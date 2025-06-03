import unittest
import numpy as np
import pandas as pd
from riemannian_stats import riemannian_analysis


class TestRiemannianUMAPAnalysis(unittest.TestCase):
    """
    Unit test suite for the RiemannianAnalysis class.

    This class contains unit tests to validate the behavior and correctness
    of the methods defined in RiemannianUMAPAnalysis, especially the computation
    of the UMAP similarity graph.
    """

    def setUp(self):
        """
        setUp method runs before each test.

        It initializes a test DataFrame with 10 samples and 2 features.
        An instance of RiemannianUMAPAnalysis is created with a small number
        of neighbors (n_neighbors=2) to simplify and control the test conditions.
        """
        self.data = pd.DataFrame(
            {
                "a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "b": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            }
        )
        self.analysis = riemannian_analysis(self.data, n_neighbors=2)

    def test_calculate_umap_graph_similarities(self):
        """
        Test the output type and shape of the UMAP similarity matrix.

        This test ensures that the method calculate_umap_graph_similarities
        returns a NumPy array and that its shape corresponds to the number of samples.
        """
        sim_matrix = self.analysis.umap_similarities
        n = self.data.shape[0]
        self.assertIsInstance(sim_matrix, np.ndarray)
        self.assertEqual(
            sim_matrix.shape, (n, n), "The similarity matrix must have shape (n, n)"
        )

    def test_result_calculate_umap_graph_similarities(self):
        """
        Test the content of the UMAP similarity matrix against a known result.

        This test compares the computed similarity matrix to a predefined expected matrix.
        It uses a small, controlled example where the structure of the UMAP graph is known.
        The result is validated with floating-point tolerance using numpy's assert_allclose.
        """
        sim_matrix = self.analysis.umap_similarities
        expected_sim_matrix = np.array(
            [
                [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
            ]
        )
        np.testing.assert_allclose(
            sim_matrix,
            expected_sim_matrix,
            rtol=1e-5,
            atol=1e-5,
            err_msg="UMAP similarity matrix does not match the expected values.",
        )

    def test_calculate_rho_matrix(self):
        """
        Test that the Rho matrix is correctly computed as 1 minus the similarity matrix.

        This test first computes the UMAP similarity matrix, then calls calculate_rho_matrix
        and validates that each element is equal to 1 - similarity[i, j] using a floating-point
        comparison with numpy's assert_allclose.
        """
        sim_matrix = self.analysis.umap_similarities
        rho_matrix = self.analysis.rho
        np.testing.assert_allclose(rho_matrix, 1 - sim_matrix)

    def test_result_calculate_rho_matrix(self):
        """
        Validate that the computed Rho matrix matches a known expected result.

        This test uses a predefined matrix representing the correct output as per
        Example 1 in 'out.pdf'. It ensures the Rho matrix conforms exactly to the
        expected values based on the UMAP similarity matrix.
        """
        rho_matrix = self.analysis.rho

        expected_rho_matrix = np.array(
            [
                [1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
            ]
        )
        np.testing.assert_allclose(
            rho_matrix,
            expected_rho_matrix,
            rtol=1e-5,
            atol=1e-5,
            err_msg="Rho matrix does not match the expected values.",
        )

    def test_riemannian_vector_difference(self):
        """
        Test that the riemannian_vector_difference returns an array with correct shape and content.

        This test checks:
        1. That the returned array is 3D with shape (n_samples, n_samples, n_features).
        2. That the Riemannian difference between specific pairs (e.g., index 0 and 1) is correctly computed
           as: rho[i,j] * (data[i] - data[j]).
        """
        riemann_diff = self.analysis.riemannian_diff
        n = self.data.shape[0]
        features = self.data.shape[1]
        self.assertEqual(
            riemann_diff.shape,
            (n, n, features),
            "The array of Riemannian differences must have shape (n, n, features)",
        )
        expected = (
            self.analysis.rho[0, 1] * (self.data.iloc[0] - self.data.iloc[1]).values
        )
        np.testing.assert_allclose(riemann_diff[0, 1], expected)

    def test_result_riemannian_vector_difference(self):
        """
        Confirm the Riemannian vector differences match a known reference array.

        This test uses a hard-coded 10x10x2 array that encodes the correct differences
        between pairs of data points scaled by the Rho matrix. This ensures that the
        implementation behaves exactly as intended.
        """

        diff_3d = self.analysis.riemannian_diff

        expected_diff = np.array(
            [
                [
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [-2.0, -2.0],
                    [-3.0, -3.0],
                    [-4.0, -4.0],
                    [-5.0, -5.0],
                    [-6.0, -6.0],
                    [-7.0, -7.0],
                    [-8.0, -8.0],
                    [-9.0, -9.0],
                ],
                [
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [-2.0, -2.0],
                    [-3.0, -3.0],
                    [-4.0, -4.0],
                    [-5.0, -5.0],
                    [-6.0, -6.0],
                    [-7.0, -7.0],
                    [-8.0, -8.0],
                ],
                [
                    [2.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [-2.0, -2.0],
                    [-3.0, -3.0],
                    [-4.0, -4.0],
                    [-5.0, -5.0],
                    [-6.0, -6.0],
                    [-7.0, -7.0],
                ],
                [
                    [3.0, 3.0],
                    [2.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [-2.0, -2.0],
                    [-3.0, -3.0],
                    [-4.0, -4.0],
                    [-5.0, -5.0],
                    [-6.0, -6.0],
                ],
                [
                    [4.0, 4.0],
                    [3.0, 3.0],
                    [2.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [-2.0, -2.0],
                    [-3.0, -3.0],
                    [-4.0, -4.0],
                    [-5.0, -5.0],
                ],
                [
                    [5.0, 5.0],
                    [4.0, 4.0],
                    [3.0, 3.0],
                    [2.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [-2.0, -2.0],
                    [-3.0, -3.0],
                    [-4.0, -4.0],
                ],
                [
                    [6.0, 6.0],
                    [5.0, 5.0],
                    [4.0, 4.0],
                    [3.0, 3.0],
                    [2.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [-2.0, -2.0],
                    [-3.0, -3.0],
                ],
                [
                    [7.0, 7.0],
                    [6.0, 6.0],
                    [5.0, 5.0],
                    [4.0, 4.0],
                    [3.0, 3.0],
                    [2.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [-2.0, -2.0],
                ],
                [
                    [8.0, 8.0],
                    [7.0, 7.0],
                    [6.0, 6.0],
                    [5.0, 5.0],
                    [4.0, 4.0],
                    [3.0, 3.0],
                    [2.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                ],
                [
                    [9.0, 9.0],
                    [8.0, 8.0],
                    [7.0, 7.0],
                    [6.0, 6.0],
                    [5.0, 5.0],
                    [4.0, 4.0],
                    [3.0, 3.0],
                    [2.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 0.0],
                ],
            ]
        )
        np.testing.assert_allclose(
            diff_3d,
            expected_diff,
            rtol=1e-5,
            atol=1e-5,
            err_msg="Riemannian vector differences do not match the expected values.",
        )

    def test_calculate_umap_distance_matrix(self):
        """
        Verifies that the UMAP distance matrix is computed correctly.

        The test ensures:
        - The shape of the resulting matrix is (n_samples, n_samples).
        - The value at a selected index (e.g., [0, 1]) matches the Euclidean norm
          of the difference vector computed by riemannian_vector_difference.
        """
        dist_matrix = self.analysis.umap_distance_matrix
        n = self.data.shape[0]
        self.assertEqual(
            dist_matrix.shape, (n, n), "The distance matrix must have shape (n, n)"
        )
        diff = self.analysis.riemannian_diff[0, 1]
        expected_norm = np.linalg.norm(diff)
        self.assertAlmostEqual(dist_matrix[0, 1], expected_norm, places=5)

    def test_result_calculate_umap_distance_matrix(self):
        """
        Confirms that the full UMAP distance matrix matches the expected result.

        This test compares the computed matrix to a predefined 10x10 distance matrix
        with known values from Example 1 in the reference document. The comparison
        uses a strict floating-point tolerance.
        """

        dist_matrix = self.analysis.umap_distance_matrix

        expected_dist_matrix = np.array(
            [
                [
                    0.0,
                    0.0,
                    2.82842712,
                    4.24264069,
                    5.65685425,
                    7.07106781,
                    8.48528137,
                    9.89949494,
                    11.3137085,
                    12.72792206,
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    2.82842712,
                    4.24264069,
                    5.65685425,
                    7.07106781,
                    8.48528137,
                    9.89949494,
                    11.3137085,
                ],
                [
                    2.82842712,
                    0.0,
                    0.0,
                    0.0,
                    2.82842712,
                    4.24264069,
                    5.65685425,
                    7.07106781,
                    8.48528137,
                    9.89949494,
                ],
                [
                    4.24264069,
                    2.82842712,
                    0.0,
                    0.0,
                    0.0,
                    2.82842712,
                    4.24264069,
                    5.65685425,
                    7.07106781,
                    8.48528137,
                ],
                [
                    5.65685425,
                    4.24264069,
                    2.82842712,
                    0.0,
                    0.0,
                    0.0,
                    2.82842712,
                    4.24264069,
                    5.65685425,
                    7.07106781,
                ],
                [
                    7.07106781,
                    5.65685425,
                    4.24264069,
                    2.82842712,
                    0.0,
                    0.0,
                    0.0,
                    2.82842712,
                    4.24264069,
                    5.65685425,
                ],
                [
                    8.48528137,
                    7.07106781,
                    5.65685425,
                    4.24264069,
                    2.82842712,
                    0.0,
                    0.0,
                    0.0,
                    2.82842712,
                    4.24264069,
                ],
                [
                    9.89949494,
                    8.48528137,
                    7.07106781,
                    5.65685425,
                    4.24264069,
                    2.82842712,
                    0.0,
                    0.0,
                    0.0,
                    2.82842712,
                ],
                [
                    11.3137085,
                    9.89949494,
                    8.48528137,
                    7.07106781,
                    5.65685425,
                    4.24264069,
                    2.82842712,
                    0.0,
                    0.0,
                    0.0,
                ],
                [
                    12.72792206,
                    11.3137085,
                    9.89949494,
                    8.48528137,
                    7.07106781,
                    5.65685425,
                    4.24264069,
                    2.82842712,
                    0.0,
                    0.0,
                ],
            ]
        )

        np.testing.assert_allclose(
            dist_matrix,
            expected_dist_matrix,
            rtol=1e-5,
            atol=1e-5,
            err_msg="UMAP distance matrix does not match the expected values.",
        )

    def test_riemannian_covariance_matrix(self):
        """
        Test the shape of the Riemannian covariance matrix.

        This test confirms that the matrix returned by riemannian_covariance_matrix
        is square and its dimensions match the number of features in the dataset.
        """
        cov_matrix = self.analysis._riemannian_covariance_matrix()
        features = self.data.shape[1]
        self.assertEqual(
            cov_matrix.shape,
            (features, features),
            "The covariance matrix must be square with dimensions (features, features)",
        )

    def test_result_riemannian_covariance_matrix(self):
        """
        Check that the computed Riemannian covariance matrix matches a known reference.

        This test compares the calculated covariance matrix to a predefined matrix
        based on the values expected from Example 1 in the documentation. Ensures
        full accuracy within floating-point tolerance.
        """
        cov_matrix = self.analysis._riemannian_covariance_matrix()

        expected_cov_matrix = np.array([[8.3, 8.3], [8.3, 8.3]])

        np.testing.assert_allclose(
            cov_matrix,
            expected_cov_matrix,
            rtol=1e-5,
            atol=1e-5,
            err_msg="Riemannian covariance matrix does not match the expected values.",
        )

    def test_riemannian_covariance_matrix_general(self):
        """
        Verifies that the general Riemannian covariance matrix is computed correctly.

        This test uses a combined DataFrame made from the original data and dummy
        components. It ensures the output matrix has the correct square shape
        (n_features x n_features), where n_features includes both original and component variables.
        """
        dummy_components = pd.DataFrame(
            {"comp1": [0.1, 0.2, 0.3], "comp2": [0.4, 0.5, 0.6]}
        )
        combined_data = pd.concat([self.data, dummy_components], axis=1)
        cov_matrix_general = self.analysis._riemannian_covariance_matrix_general(
            combined_data
        )
        n_features = combined_data.shape[1]
        self.assertEqual(
            cov_matrix_general.shape,
            (n_features, n_features),
            "The general covariance matrix must have dimensions (n_features, n_features)",
        )

    def test_riemannian_correlation_matrix(self):
        """
        Verifies the shape and basic properties of the Riemannian correlation matrix.

        This test confirms that:
        - The correlation matrix has dimensions equal to the number of features.
        - The diagonal elements (self-correlations) are approximately 1.0.
        """
        corr_matrix = self.analysis.riemannian_correlation_matrix()
        features = self.data.shape[1]
        self.assertEqual(
            corr_matrix.shape,
            (features, features),
            "The correlation matrix must have dimensions (features, features)",
        )
        for i in range(features):
            self.assertAlmostEqual(corr_matrix[i, i], 1.0, places=5)

    def test_result_riemannian_correlation_matrix(self):
        """
        Verifies that the computed Riemannian correlation matrix matches a known expected result.

        This test checks against a predefined matrix from Example 1 and ensures all values match
        within a floating-point tolerance.
        """
        corr_matrix = self.analysis.riemannian_correlation_matrix()
        expected_corr_matrix = np.array([[1.0, 1.0], [1.0, 1.0]])

        np.testing.assert_allclose(
            corr_matrix,
            expected_corr_matrix,
            rtol=1e-5,
            atol=1e-5,
            err_msg="Riemannian correlation matrix does not match the expected values.",
        )

    def test_riemannian_components_from_data_and_correlation(self):
        """
        Verifies that the principal components matrix from Riemannian PCA has the expected shape.

        The matrix should have shape (n_samples, n_features), representing the projection
        of the original data into principal component space using the provided correlation matrix.
        """
        corr_matrix = self.analysis.riemannian_correlation_matrix()
        components = self.analysis.riemannian_components_from_data_and_correlation(
            corr_matrix
        )
        n = self.data.shape[0]
        features = self.data.shape[1]
        self.assertEqual(
            components.shape,
            (n, features),
            "The components matrix must have shape (n_samples, n_features)",
        )

    def test_result_riemannian_components_from_data_and_correlation(self):
        """
        Verifies that the computed Riemannian principal components match the expected values.

        This test checks that the result of riemannian_components_from_data_and_correlation
        aligns with a known matrix of principal components (as defined in a reference PDF).
        The comparison uses a strict floating-point tolerance to ensure numerical correctness.
        """
        corr_matrix = self.analysis.riemannian_correlation_matrix()
        components = self.analysis.riemannian_components_from_data_and_correlation(
            corr_matrix
        )

        expected_components = np.array(
            [
                [-1.96352277e00, 8.81429070e-18],
                [-1.47264208e00, 3.91283976e-17],
                [-9.81761387e-01, 4.40714535e-18],
                [0.00000000e00, 0.00000000e00],
                [0.00000000e00, 0.00000000e00],
                [0.00000000e00, 0.00000000e00],
                [9.81761387e-01, -4.40714535e-18],
                [1.47264208e00, -3.91283976e-17],
                [1.96352277e00, -8.81429070e-18],
                [2.45440347e00, 6.74867596e-17],
            ]
        )

        np.testing.assert_allclose(
            components,
            expected_components,
            rtol=1e-5,
            atol=1e-5,
            err_msg="Riemannian components from data and correlation do not match the expected values.",
        )

    def test_riemannian_components(self):
        """
        Verifies that the riemannian_components method returns a matrix with the correct shape.

        The expected shape of the returned matrix is (n_samples, n_features),
        confirming that the PCA transformation was applied correctly.
        """
        corr_matrix = self.analysis.riemannian_correlation_matrix()
        components = self.analysis.riemannian_components(corr_matrix)
        n = self.data.shape[0]
        features = self.data.shape[1]
        self.assertEqual(
            components.shape,
            (n, features),
            "The riemannian_components function must return a matrix with shape (n, features)",
        )

    def test_riemannian_correlation_variables_components(self):
        """
        Verifies the structure of the DataFrame returned by riemannian_correlation_variables_components.

        The resulting DataFrame should:
        - Have one row per original feature.
        - Contain two columns labeled 'Component_1' and 'Component_2'.
        This ensures consistency in downstream interpretation of component-variable correlations.
        """
        corr_matrix = self.analysis.riemannian_correlation_matrix()
        components = self.analysis.riemannian_components_from_data_and_correlation(
            corr_matrix
        )
        correlations_df = self.analysis.riemannian_correlation_variables_components(
            components
        )
        self.assertEqual(
            correlations_df.shape[0],
            self.data.shape[1],
            "The number of rows in the DataFrame must equal the number of features",
        )
        self.assertListEqual(
            list(correlations_df.columns),
            ["Component_1", "Component_2"],
            "The columns must be ['Component_1', 'Component_2']",
        )

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
        # Construye DataFrame combinado
        combined_data = pd.DataFrame(
            np.hstack((self._data, components[:, 0:2])),
            columns=[f"feature_{i + 1}" for i in range(self._data.shape[1])]
            + ["Component_1", "Component_2"],
        )

        # Calcula matriz de covarianza riemanniana
        riemannian_cov_matrix = self._riemannian_covariance_matrix_general(
            combined_data
        )

        # Inicializa DataFrame de correlaciones
        correlations = pd.DataFrame(
            index=[f"feature_{i + 1}" for i in range(self._data.shape[1])],
            columns=["Component_1", "Component_2"],
            dtype=np.float64,
        )

        # Calcula correlaciones para Component_1
        for i in range(self._data.shape[1]):
            denom = np.sqrt(riemannian_cov_matrix[i, i] * riemannian_cov_matrix[-2, -2])
            if denom != 0:
                correlations.loc[f"feature_{i + 1}", "Component_1"] = (
                    riemannian_cov_matrix[i, -2] / denom
                )
            else:
                correlations.loc[f"feature_{i + 1}", "Component_1"] = 0.0

        # Calcula correlaciones para Component_2
        for i in range(self._data.shape[1]):
            denom = np.sqrt(riemannian_cov_matrix[i, i] * riemannian_cov_matrix[-1, -1])
            if denom != 0:
                correlations.loc[f"feature_{i + 1}", "Component_2"] = (
                    riemannian_cov_matrix[i, -1] / denom
                )
            else:
                correlations.loc[f"feature_{i + 1}", "Component_2"] = 0.0

        return correlations


if __name__ == "__main__":
    unittest.main()
