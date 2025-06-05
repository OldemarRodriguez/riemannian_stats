import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
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

    @staticmethod
    def get_custom_palette():
        """
        Returns a custom color palette without black and white.

        Returns:
            ListedColormap: A colormap based on a custom list of colors.
        """
        my_custom_palette = [
            "#5F9EA0", "#7FFF00", "#D2691E", "#FF7F50", "#6495ED", "#FFF8DC",
            "#DC143C", "#00FFFF", "#00008B", "#008B8B", "#B8860B", "#A9A9A9",
            "#006400", "#BDB76B", "#8B008B", "#556B2F", "#FF8C00", "#9932CC",
            "#8B0000", "#E9967A", "#8FBC8F", "#483D8B", "#2F4F4F", "#00CED1",
            "#9400D3", "#FF1493", "#00BFFF", "#696969", "#1E90FF", "#B22222",
            "#FFFAF0", "#228B22", "#FF00FF", "#DCDCDC", "#F8F8FF", "#FFD700",
            "#DAA520", "#808080", "#008000", "#ADFF2F", "#F0FFF0", "#FF69B4",
            "#CD5C5C", "#4B0082", "#FFFFF0", "#F0E68C", "#E6E6FA", "#FFF0F5",
            "#7CFC00", "#FFFACD", "#ADD8E6", "#F08080", "#E0FFFF", "#FAFAD2",
            "#D3D3D3", "#90EE90", "#FFB6C1", "#FFA07A", "#20B2AA", "#87CEFA",
            "#778899", "#B0C4DE", "#FFFFE0", "#00FF00", "#32CD32", "#FAF0E6",
            "#FF00FF", "#800000", "#66CDAA", "#0000CD", "#BA55D3", "#9370D8",
            "#3CB371", "#7B68EE", "#00FA9A", "#48D1CC", "#C71585", "#191970",
            "#F5FFFA", "#FFE4E1", "#FFE4B5", "#FFDEAD", "#000080", "#FDF5E6",
            "#808000", "#6B8E23", "#FFA500", "#FF4500", "#DA70D6", "#EEE8AA",
            "#98FB98", "#AFEEEE", "#D87093", "#FFEFD5", "#FFDAB9", "#CD853F",
            "#FFC0CB", "#DDA0DD", "#B0E0E6", "#800080", "#FF0000", "#BC8F8F",
            "#4169E1", "#8B4513", "#FA8072", "#F4A460", "#2E8B57", "#FFF5EE",
            "#A0522D", "#C0C0C0", "#87CEEB", "#6A5ACD", "#708090", "#FFFAFA",
            "#00FF7F", "#4682B4", "#D2B48C", "#008080", "#D8BFD8", "#FF6347",
            "#40E0D0", "#EE82EE", "#F5DEB3", "#F5F5F5", "#FFFF00", "#9ACD32"
        ]
        return mcolors.ListedColormap(my_custom_palette)

    @staticmethod
    def get_adaptive_colormap(n_clusters: int):
        """
        Returns an adaptive colormap based on the number of clusters.
        This version uses the custom palette defined in the get_custom_palette method.

        Parameters:
            n_clusters (int): The number of clusters that need unique colors.

        Returns:
            ListedColormap: A colormap that contains a sufficient number of distinct colors for the given clusters.
        """
        # Get the custom palette (without black and white)
        custom_palette = Utilities.get_custom_palette()

        # Limit the number of colors to n_clusters
        if n_clusters <= len(custom_palette.colors):
            return plt.cm.colors.ListedColormap(custom_palette.colors[:n_clusters])
        else:
            raise ValueError(f"Requested more colors ({n_clusters}) than available in the custom palette.")