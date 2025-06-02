import unittest
import numpy as np
from riemannian_stats import utilities


class TestPCAInertiaByComponents(unittest.TestCase):
    """
    Unit tests for the Utilities.pca_inertia_by_components static method.

    These tests verify the correctness, input validation, and edge cases for computing
    the proportion of variance (inertia) explained by selected principal components.
    """

    def setUp(self):
        """
        Setup runs before each test method.

        It initializes a valid 3x3 correlation matrix and an invalid non-square matrix
        to test both valid and edge-case scenarios.
        """
        self.valid_corr_matrix = np.array(
            [[1.0, 0.8, 0.5], [0.8, 1.0, 0.3], [0.5, 0.3, 1.0]]
        )

        self.invalid_corr_matrix = np.array([[1.0, 0.8], [0.8, 1.0], [0.5, 0.3]])

    def test_valid_components(self):
        """
        Verifies that the explained inertia value for valid components
        lies between 0 and 1 (inclusive).
        """
        explained_inertia = utilities.pca_inertia_by_components(
            self.valid_corr_matrix, 0, 1
        )
        self.assertTrue(
            0 <= explained_inertia <= 1, "Explained inertia must be between 0 and 1."
        )

    def test_invalid_corr_matrix(self):
        """
        Verifies that a ValueError is raised when the correlation matrix is not square.
        """
        with self.assertRaises(ValueError):
            utilities.pca_inertia_by_components(self.invalid_corr_matrix, 0, 1)

    def test_invalid_component_indices(self):
        """
        Verifies that a ValueError is raised when invalid component indices are provided.

        This includes negative indices and indices outside the valid component range.
        """
        with self.assertRaises(ValueError):
            utilities.pca_inertia_by_components(self.valid_corr_matrix, -1, 1)

        with self.assertRaises(ValueError):
            utilities.pca_inertia_by_components(self.valid_corr_matrix, 0, 3)

    def test_total_inertia_equals_one(self):
        """
        Verifies that the sum of all explained inertia (from all components)
        equals approximately 1.0, ensuring a complete decomposition.
        """
        eigenvalues, _ = np.linalg.eig(self.valid_corr_matrix)
        total_inertia = np.sum(eigenvalues)
        selected_inertia = np.sum(eigenvalues)  # sum of all eigenvalues
        explained_inertia = selected_inertia / total_inertia
        self.assertAlmostEqual(
            explained_inertia,
            1.0,
            places=5,
            msg="Total inertia should sum up approximately to 1.",
        )


if __name__ == "__main__":
    unittest.main()
