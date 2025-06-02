import numpy as np

import numpy as np


class Utilities:
    """
    Class for common utility functions in data science projects.

    Provides static methods for mathematical or statistical operations,
    such as PCA-based calculations, designed to support data analysis pipelines
    without requiring class instantiation.
    """

    @staticmethod
    def pca_inertia_by_components(
        correlation_matrix: np.ndarray, component1: int, component2: int
    ) -> float:
        """
        Calculates the inertia (explained variance ratio) of two specified principal components from a correlation matrix.

        Parameters:
            correlation_matrix (np.ndarray): Square correlation matrix used in PCA.
            component1 (int): Index of the first principal component (0-based, after sorting by eigenvalue).
            component2 (int): Index of the second principal component (0-based, after sorting by eigenvalue).

        Returns:
            float: The proportion of total variance explained by the two components (value between 0 and 1).

        Raises:
            ValueError: If the correlation matrix is not square or if the component indices are out of bounds.
        """
        if correlation_matrix.shape[0] != correlation_matrix.shape[1]:
            raise ValueError("The correlation matrix must be square.")

        if not (0 <= component1 < correlation_matrix.shape[0]) or not (
            0 <= component2 < correlation_matrix.shape[0]
        ):
            raise ValueError("Component indices are out of bounds.")

        eigenvalues, _ = np.linalg.eig(correlation_matrix)
        sorted_eigenvalues = np.sort(eigenvalues)[::-1]

        total_inertia = np.sum(sorted_eigenvalues)
        selected_inertia = (
            sorted_eigenvalues[component1] + sorted_eigenvalues[component2]
        )
        return selected_inertia / total_inertia
