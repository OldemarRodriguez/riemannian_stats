import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend for test environments

import matplotlib.pyplot as plt
import pytest
import unittest
import pandas as pd
import numpy as np
from riemannian_stats.visualization import Visualization


class TestVisualization(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame(
            {
                "feature1": [1.0, 2.0, 3.0],
                "feature2": [4.0, 5.0, 6.0],
                "feature3": [7.0, 8.0, 9.0],
                "species": ["A", "B", "C"],
            },
            index=["sample1", "sample2", "sample3"],
        )

        self.components = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])

        self.correlations = pd.DataFrame({0: [0.8, 0.3, -0.5], 1: [-0.4, 0.9, 0.2]}).T

        self.explained_inertia = 75.0
        self.clusters = np.array(["A", "B", "C"])

    def tearDown(self):
        # Close all matplotlib figures to avoid memory or backend issues
        plt.close("all")

    def test_create_visualization_object(self):
        viz = Visualization(
            self.data, self.components, self.explained_inertia, self.clusters
        )
        self.assertIsInstance(viz, Visualization)
        self.assertEqual(viz.explained_inertia, 75.0)

    def test_plot_principal_plane(self):
        viz = Visualization(self.data, self.components, self.explained_inertia)
        try:
            viz.plot_principal_plane(title="Test Principal Plane")
        except Exception as e:
            self.fail(f"plot_principal_plane raised an exception: {e}")

    def test_plot_principal_plane_with_clusters(self):
        viz = Visualization(
            self.data, self.components, self.explained_inertia, self.clusters
        )
        try:
            viz.plot_principal_plane_with_clusters(title="Test Plane with Clusters")
        except Exception as e:
            self.fail(f"plot_principal_plane_with_clusters raised an exception: {e}")

    def test_plot_2d_scatter_with_clusters(self):
        viz = Visualization(
            self.data, self.components, self.explained_inertia, self.clusters
        )
        try:
            viz.plot_2d_scatter_with_clusters(
                "feature1", "feature2", "species", title="2D Scatter Test"
            )
        except Exception as e:
            self.fail(f"plot_2d_scatter_with_clusters raised an exception: {e}")

    def test_plot_3d_scatter_with_clusters(self):
        viz = Visualization(
            self.data, self.components, self.explained_inertia, self.clusters
        )
        try:
            viz.plot_3d_scatter_with_clusters(
                "feature1", "feature2", "feature3", "species", title="3D Scatter Test"
            )
        except Exception as e:
            self.fail(f"plot_3d_scatter_with_clusters raised an exception: {e}")

    @pytest.mark.xfail(reason="Fails intermittently due to matplotlib backend")
    def test_plot_correlation_circle(self):
        # TODO: Fix this flaky test related to matplotlib interaction
        viz = Visualization(self.data, self.components, self.explained_inertia)
        try:
            viz.plot_correlation_circle(
                self.correlations.T, title="Correlation Circle Test"
            )
        except Exception as e:
            self.fail(f"plot_correlation_circle raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
