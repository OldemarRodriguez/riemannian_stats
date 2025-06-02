from typing import Union, Optional
import matplotlib

matplotlib.use("TkAgg")  # Alternatively, you can try 'Agg', 'Qt5Agg', 'GTK3Agg', etc.
import umap
import pandas as pd
import numpy as np


class RiemannianAnalysis:
    """
    A class to perform UMAP-based analysis combined with Riemannian geometry.

    This class allows dimensionality reduction, similarity graph analysis, and custom covariance/correlation
    computations using a Riemannian-weighted framework, enhancing traditional UMAP with structure-aware geometry.

    Parameters:
        data (np.ndarray or pd.DataFrame): Input dataset.
        n_neighbors (int): Number of neighbors for UMAP KNN graph construction. Default is 3.
        min_dist (float): Minimum distance parameter for UMAP, controlling cluster tightness. Default is 0.1.
        metric (str): Distance metric for UMAP (e.g., "euclidean", "manhattan"). Default is "euclidean".

    Properties:
        data (np.ndarray or pd.DataFrame): The input data. Setting this triggers automatic recomputation of all derived matrices.
        n_neighbors (int): Number of neighbors for UMAP. Setting this re-triggers internal recomputations.
        min_dist (float): Minimum distance used in UMAP embedding. Automatically recomputes internal matrices on change.
        metric (str): UMAP distance metric. Triggers recomputation if modified.

        umap_similarities (np.ndarray): Matrix of similarity values from the UMAP fuzzy graph.
        rho (np.ndarray): Matrix computed as (1 - UMAP similarity), used to weight vector differences.
        riemannian_diff (np.ndarray): 3D array of weighted pairwise vector differences between observations.
        umap_distance_matrix (np.ndarray): Pairwise distance matrix computed from Riemannian differences.

    Methods:
        riemannian_correlation_matrix() -> np.ndarray:
            Computes the correlation matrix based on the Riemannian covariance structure.

        riemannian_components(corr_matrix: np.ndarray) -> np.ndarray:
            Performs Riemannian PCA using the supplied correlation matrix.

        riemannian_components_from_data_and_correlation(corr_matrix: np.ndarray) -> np.ndarray:
            Like `riemannian_components`, but uses both data and a given correlation matrix.

        riemannian_correlation_variables_components(components: np.ndarray) -> pd.DataFrame:
            Calculates Riemannian correlations between original features and the first two components.

    Notes:
        - Setting `data`, `n_neighbors`, `min_dist`, or `metric` automatically recalculates:
            - UMAP similarities
            - Rho matrix
            - Riemannian differences
            - UMAP distance matrix
        - Internal methods (prefixed with double underscores) are used for computing intermediate matrices and are not intended for external use.
    """

    def __init__(
        self,
        data: Union[np.ndarray, pd.DataFrame],
        n_neighbors: int = 3,
        min_dist: float = 0.1,
        metric: str = "euclidean",
    ) -> None:
        """
        Initialize the RiemannianAnalysis object with data and UMAP parameters.

        Parameters:
            data (Union[np.ndarray, pd.DataFrame]): Input dataset where rows represent observations and
                columns represent features. It is internally stored and accessible via a read/write property.
            n_neighbors (int): Number of neighbors to use for local connectivity in UMAP. Default is 3.
            min_dist (float): Minimum distance between embedded points in UMAP space. Default is 0.1.
            metric (str): Distance metric for UMAP. Common options include "euclidean", "manhattan", etc. Default is "euclidean".

        Behavior:
            Upon instantiation, the class computes:
               - The UMAP similarity matrix (from the fuzzy KNN graph)
               - The Rho matrix (1 - similarity)
               - The Riemannian difference tensor (weighted differences between data points)
               - The UMAP distance matrix (based on the Riemannian differences)

            These matrices are automatically recomputed if any of the following attributes are modified:
               - data
               - n_neighbors
               - min_dist
               - metric

        Raises:
                ValueError: Raised later in methods if necessary preconditions (e.g., valid matrix shapes) are not met.

        Notes:
            - Internally stores data and parameters as protected attributes (_data, _n_neighbors, etc.).
            - Uses double-underscore methods for internal computation (_Riemannian differences, UMAP graph, etc.).
            - Properties provide read-only access to computed matrices: `umap_similarities`, `rho`, `riemannian_diff`, and `umap_distance_matrix`.
        """
        self._data = data
        self._n_neighbors = n_neighbors
        self._min_dist = min_dist
        self._metric = metric
        self.__umap_similarities: Union[np.ndarray, None] = (
            self.__calculate_umap_graph_similarities()
        )
        self.__rho: Union[np.ndarray, None] = self.__calculate_rho_matrix()
        self.__riemannian_diff: Union[np.ndarray, None] = (
            self.__riemannian_vector_difference()
        )
        self.__umap_distance_matrix: Union[np.ndarray, None] = (
            self.__calculate_umap_distance_matrix()
        )

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: Union[np.ndarray, pd.DataFrame]):
        self._data = value
        self.__recompute()

    @property
    def n_neighbors(self):
        return self._n_neighbors

    @n_neighbors.setter
    def n_neighbors(self, value: int):
        self._n_neighbors = value
        self.__recompute()

    @property
    def min_dist(self):
        return self._min_dist

    @min_dist.setter
    def min_dist(self, value: float):
        self._min_dist = value
        self.__recompute()

    @property
    def metric(self):
        return self._metric

    @metric.setter
    def metric(self, value: str):
        self._metric = value
        self.__recompute()

    @property
    def umap_similarities(self) -> Optional[np.ndarray]:
        """Returns the UMAP similarity matrix."""
        return self.__umap_similarities

    @property
    def rho(self) -> Optional[np.ndarray]:
        """Returns the Rho matrix (1 - UMAP similarities)."""
        return self.__rho

    @property
    def riemannian_diff(self) -> Optional[np.ndarray]:
        """Returns the 3D array of weighted Riemannian differences."""
        return self.__riemannian_diff

    @property
    def umap_distance_matrix(self) -> Optional[np.ndarray]:
        """Returns the UMAP distance matrix."""
        return self.__umap_distance_matrix

    def __recompute(self):
        """Recompute all derived matrices when input parameters change."""
        self.__umap_similarities = self.__calculate_umap_graph_similarities()
        self.__rho = self.__calculate_rho_matrix()
        self.__riemannian_diff = self.__riemannian_vector_difference()
        self.__umap_distance_matrix = self.__calculate_umap_distance_matrix()

    def __calculate_umap_graph_similarities(self) -> np.ndarray:
        """
        Calculates UMAP similarities based on the KNN connectivity graph.

        Returns:
            numpy.ndarray: UMAP similarity matrix derived from the KNN graph.
        """
        reducer = umap.UMAP(
            n_neighbors=self._n_neighbors, min_dist=self._min_dist, metric=self._metric
        )
        reducer.fit(self._data)
        umap_graph = reducer.graph_
        umap_similarities = np.array(umap_graph.todense())
        return umap_similarities

    def __calculate_rho_matrix(self) -> np.ndarray:
        """
        Calculates the Rho matrix as 1 minus the UMAP similarity matrix.

        Returns:
            numpy.ndarray: Rho matrix.

        Raises:
            ValueError: If UMAP similarities have not been calculated.
        """
        if self.umap_similarities is None:
            raise ValueError(
                "UMAP similarities must be calculated before obtaining the Rho matrix."
            )
        rho = 1 - self.umap_similarities
        return rho

    def __riemannian_vector_difference(self) -> np.ndarray:
        """
        Calculates the Riemannian difference between each pair of row vectors in the data matrix.

        Returns:
            numpy.ndarray: 3D array containing the Riemannian differences for each pair of rows.

        Raises:
            ValueError: If the Rho matrix has not been calculated.
        """
        if self.rho is None:
            raise ValueError(
                "Rho matrix must be calculated before computing Riemannian differences."
            )
        n_rows = self._data.shape[0]
        riemannian_diff = np.zeros((n_rows, n_rows, self._data.shape[1]))
        for i in range(n_rows):
            for j in range(n_rows):
                riemannian_diff[i, j] = self.rho[i, j] * (
                    self._data.iloc[i] - self._data.iloc[j]
                )
        return riemannian_diff

    def __calculate_umap_distance_matrix(self) -> np.ndarray:
        """
        Calculates the UMAP distance matrix using weighted Riemannian differences.

        Returns:
            numpy.ndarray: UMAP distance matrix.

        Raises:
            ValueError: If the Riemannian differences have not been calculated.
        """
        if self.riemannian_diff is None:
            raise ValueError(
                "Riemannian differences must be calculated before obtaining the UMAP distance matrix."
            )
        n_rows = self.riemannian_diff.shape[0]
        umap_distance_matrix = np.zeros((n_rows, n_rows))
        for i in range(n_rows):
            for j in range(n_rows):
                umap_distance_matrix[i, j] = np.linalg.norm(self.riemannian_diff[i, j])
        return umap_distance_matrix

    def _riemannian_covariance_matrix(self) -> np.ndarray:
        """
        Calculates the covariance matrix using Riemannian differences.

        Returns:
            numpy.ndarray: Riemannian covariance matrix.

        Raises:
            ValueError: If the UMAP distance matrix has not been calculated.
        """
        if self.umap_distance_matrix is None:
            raise ValueError(
                "UMAP distance matrix must be calculated before obtaining the Riemannian covariance matrix."
            )
        riemannian_mean_index = np.argmin(np.sum(self.umap_distance_matrix, axis=1))
        n_samples, n_features = self._data.shape
        cov_matrix = np.zeros((n_features, n_features))
        for i in range(n_samples):
            diff_vector = self.rho[i, riemannian_mean_index] * (
                self._data.iloc[i] - self._data.iloc[riemannian_mean_index]
            )
            cov_matrix += np.outer(diff_vector, diff_vector)
        return cov_matrix / n_samples

    def _riemannian_covariance_matrix_general(
        self, combined_data: pd.DataFrame
    ) -> np.ndarray:
        """
        Helper method to calculate the Riemannian covariance matrix for a generic dataset.

        Parameters:
            combined_data (pandas.DataFrame): Combined data (e.g., original data and components).

        Returns:
            numpy.ndarray: Riemannian covariance matrix.
        """
        riemannian_mean_index = np.argmin(np.sum(self.umap_distance_matrix, axis=1))
        n_samples, n_features = combined_data.shape
        cov_matrix = np.zeros((n_features, n_features))
        for i in range(n_samples):
            diff_vector = self.rho[i, riemannian_mean_index] * (
                combined_data.iloc[i] - combined_data.iloc[riemannian_mean_index]
            )
            cov_matrix += np.outer(diff_vector, diff_vector)
        return cov_matrix / n_samples

    def riemannian_correlation_matrix(self) -> np.ndarray:
        """
        Calculates the Riemannian correlation matrix from the Riemannian covariance matrix.

        Returns:
            numpy.ndarray: Riemannian correlation matrix.
        """
        cov_matrix_riemannian = self._riemannian_covariance_matrix()
        n = cov_matrix_riemannian.shape[0]
        corr_matrix_riemannian = np.zeros_like(cov_matrix_riemannian)
        for i in range(n):
            for j in range(n):
                corr_matrix_riemannian[i, j] = cov_matrix_riemannian[i, j] / np.sqrt(
                    cov_matrix_riemannian[i, i] * cov_matrix_riemannian[j, j]
                )
        return corr_matrix_riemannian

    def riemannian_components_from_data_and_correlation(
        self, corr_matrix: np.ndarray
    ) -> np.ndarray:
        """
        Performs Riemannian principal component analysis (PCA) using the data and the provided correlation matrix.

        Parameters:
            corr_matrix (numpy.ndarray): Correlation matrix of the variables.

        Returns:
            numpy.ndarray: Matrix of principal components.

        Raises:
            ValueError: If the correlation matrix is not square or if its size does not match the number of data columns.
        """
        if corr_matrix.shape[0] != corr_matrix.shape[1]:
            raise ValueError("The correlation matrix must be square.")
        if self._data.shape[1] != corr_matrix.shape[0]:
            raise ValueError(
                "The number of columns in the data must match the size of the correlation matrix."
            )

        riemannian_mean_index = np.argmin(np.sum(self.umap_distance_matrix, axis=1))
        riemannian_mean_centered_data = np.zeros_like(self._data)
        for i in range(self._data.shape[0]):
            riemannian_mean_centered_data[i] = self.rho[i, riemannian_mean_index] * (
                self._data.iloc[i] - self._data.iloc[riemannian_mean_index]
            )
        riemannian_std_population = np.sqrt(
            np.sum(riemannian_mean_centered_data**2, axis=0) / self._data.shape[0]
        )
        standardized_data = riemannian_mean_centered_data / riemannian_std_population

        eigenvalues, eigenvectors = np.linalg.eig(corr_matrix)
        sorted_indices = np.argsort(eigenvalues)[::-1]
        eigenvectors = eigenvectors[:, sorted_indices]
        principal_components = np.dot(standardized_data, eigenvectors)
        return principal_components

    def riemannian_components(self, corr_matrix: np.ndarray) -> np.ndarray:
        """
        Performs Riemannian principal component analysis (PCA) using the supplied correlation matrix.

        Parameters:
            corr_matrix (numpy.ndarray): Riemannian correlation matrix.

        Returns:
            numpy.ndarray: Matrix of principal components.

        Raises:
            ValueError: If the correlation matrix is not square or if its size does not match the number of data columns.
        """
        if corr_matrix.shape[0] != corr_matrix.shape[1]:
            raise ValueError("The correlation matrix must be square.")
        if self._data.shape[1] != corr_matrix.shape[0]:
            raise ValueError(
                "The number of columns in the data must match the size of the correlation matrix."
            )

        riemannian_mean_index = np.argmin(np.sum(self.umap_distance_matrix, axis=1))
        riemannian_mean_centered_data = np.zeros_like(self._data)
        for i in range(self._data.shape[0]):
            riemannian_mean_centered_data[i] = self.rho[i, riemannian_mean_index] * (
                self._data.iloc[i] - self._data.iloc[riemannian_mean_index]
            )
        riemannian_std_population = np.sqrt(
            np.sum(riemannian_mean_centered_data**2, axis=0) / self._data.shape[0]
        )
        standardized_data = riemannian_mean_centered_data / riemannian_std_population

        eigenvalues, eigenvectors = np.linalg.eig(corr_matrix)
        sorted_indices = np.argsort(eigenvalues)[::-1]
        eigenvectors = eigenvectors[:, sorted_indices]
        principal_components = np.dot(standardized_data, eigenvectors)
        return principal_components

    def riemannian_correlation_variables_components(
        self, components: np.ndarray
    ) -> pd.DataFrame:
        """
        Calculates the Riemannian correlation between the original variables and the first two components.

        Parameters:
            components (numpy.ndarray): Matrix of components (at least two columns are expected).

        Returns:
            pandas.DataFrame: DataFrame with the correlation of each original variable with the first and second components.
        """
        combined_data = pd.DataFrame(
            np.hstack((self._data, components[:, 0:2])),
            columns=[f"feature_{i + 1}" for i in range(self._data.shape[1])]
            + ["Component_1", "Component_2"],
        )
        riemannian_cov_matrix = self._riemannian_covariance_matrix_general(
            combined_data
        )
        correlations = pd.DataFrame(
            index=[f"feature_{i + 1}" for i in range(self._data.shape[1])],
            columns=["Component_1", "Component_2"],
        )
        for i in range(self._data.shape[1]):
            correlations.loc[f"feature_{i + 1}", "Component_1"] = riemannian_cov_matrix[
                i, -2
            ] / np.sqrt(riemannian_cov_matrix[i, i] * riemannian_cov_matrix[-2, -2])
        for i in range(self._data.shape[1]):
            correlations.loc[f"feature_{i + 1}", "Component_2"] = riemannian_cov_matrix[
                i, -1
            ] / np.sqrt(riemannian_cov_matrix[i, i] * riemannian_cov_matrix[-1, -1])
        return correlations
