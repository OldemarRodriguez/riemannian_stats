import os
import matplotlib

# Only set non-interactive backend in test or headless mode
if os.environ.get("DISPLAY", "") == "" or "PYTEST_CURRENT_TEST" in os.environ:
    matplotlib.use("Agg")

import unittest
import pandas as pd
from riemannian_stats import Visualization, RiemannianAnalysis, Utilities

class TestVisualization(unittest.TestCase):
    """
    Unit tests for the Visualization class.

    These tests validate that various plotting methods run without exceptions
    when provided with valid inputs, covering basic 2D/3D scatter plots,
    principal planes, and correlation visualizations.
    """

    def setUp(self):
        """
        Sets up the test environment by preparing a simple dataset and computing
        necessary components using RiemannianAnalysis. Also creates a Visualization
        instance with clustering and explained inertia.
        """
        self.data = pd.DataFrame(
            {
                "a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "b": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                "cluster": [0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            }
        )

        self.analysis = RiemannianAnalysis(self.data[["a", "b"]], n_neighbors=2)

        self.corr_matrix = self.analysis.riemannian_correlation_matrix()
        self.components = self.analysis.riemannian_components(self.corr_matrix)
        self.inertia = Utilities.pca_inertia_by_components(self.corr_matrix, 0, 1) * 100

        self.viz = Visualization(
            data=self.data,
            components=self.components,
            explained_inertia=self.inertia,
            clusters=self.data["cluster"].values,
        )

    def test_plot_principal_plane(self):
        """Test that the plot_principal_plane method executes without raising an exception."""
        try:
            self.viz.plot_principal_plane(title="Test Principal Plane")
        except Exception as e:
            self.fail(f"plot_principal_plane raised an exception unexpectedly: {e}")

    def test_plot_principal_plane_with_clusters(self):
        """Test that the plot_principal_plane_with_clusters method executes successfully with cluster coloring."""
        try:
            self.viz.plot_principal_plane_with_clusters(
                title="Test Principal Plane with Clusters"
            )
        except Exception as e:
            self.fail(f"plot_principal_plane_with_clusters raised an exception: {e}")

    def test_plot_correlation_circle(self):
        """Test that the correlation circle plot is generated successfully using variable-component correlations."""
        correlations = self.analysis.riemannian_correlation_variables_components(
            self.components
        )
        try:
            self.viz.plot_correlation_circle(
                correlations=correlations, title="Test Correlation Circle"
            )
        except Exception as e:
            self.fail(f"plot_correlation_circle raised an exception unexpectedly: {e}")

    def test_plot_2d_scatter_with_clusters(self):
        """Test that a 2D scatter plot with cluster coloring is generated without errors."""
        try:
            self.viz.plot_2d_scatter_with_clusters(
                x_col="a",
                y_col="b",
                cluster_col="cluster",
                title="Test 2D Scatter with Clusters",
            )
        except Exception as e:
            self.fail(f"plot_2d_scatter_with_clusters raised an exception: {e}")

    def test_plot_3d_scatter_with_clusters(self):
        """
        Test that a 3D scatter plot with clusters is rendered without error.

        This test extends the dataset with a third dimension and verifies
        that plot_3d_scatter_with_clusters executes successfully.
        """
        self.data["c"] = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        self.viz._data = self.data
        try:
            self.viz.plot_3d_scatter_with_clusters(
                x_col="a",
                y_col="b",
                z_col="c",
                cluster_col="cluster",
                title="Test 3D Scatter with Clusters",
            )
        except Exception as e:
            self.fail(f"plot_3d_scatter_with_clusters raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()