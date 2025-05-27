from typing import Optional, Tuple, Union
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Visualization:
    """
    A class for generating visualizations of UMAP or PCA results, including projections, clusters, and correlation circles.

    This class is designed to assist in interpreting dimensionality-reduced data through visual inspection.

    Parameters:
        data (pd.DataFrame): The dataset to be visualized (must include index and optionally cluster columns).
        components (np.ndarray, optional): Principal component matrix with at least two dimensions.
        explained_inertia (float, optional): The total explained inertia (variance) by the components.
        clusters (np.ndarray, optional): Array of cluster labels corresponding to the data rows.

    Attributes:
        data (pd.DataFrame): Read-only access to the input dataset.
        components (np.ndarray or None): Read-only access to PCA/UMAP component matrix.
        explained_inertia (float): Read-only access to the explained inertia percentage.
        clusters (np.ndarray or None): Read-only access to cluster labels.

    Methods:
        plot_principal_plane(title=""): 2D projection of the components with point labels.
        plot_principal_plane_with_clusters(title=""): Same as above, but colored by clusters.
        plot_correlation_circle(correlations, title="", scale=1, draw_circle=True): Visualizes correlation of variables.
        plot_2d_scatter_with_clusters(x_col, y_col, cluster_col, title="", figsize=(10, 8)): 2D scatter plot by cluster.
        plot_3d_scatter_with_clusters(x_col, y_col, z_col, cluster_col, title="", ...): 3D scatter plot by cluster.
    """

    def __init__(self, data: pd.DataFrame, components: Optional[np.ndarray] = None,
                 explained_inertia: float = 0.0, clusters: Optional[np.ndarray] = None) -> None:
        """
            Initializes the Visualization object with data and optional component, cluster, and variance information.

            Parameters:
                data (pd.DataFrame): The dataset to be used for plotting (index used as labels).
                components (np.ndarray, optional): Matrix of principal components or UMAP embeddings (n_samples, n_components).
                explained_inertia (float, optional): Percentage of variance explained by the components. Default is 0.0.
                clusters (np.ndarray, optional): Optional array of cluster labels aligned with data rows.

            Notes:
                - Internally uses protected attributes (_data, _components, _explained_inertia, _clusters).
                - Read-only properties are used to safely expose internal data.
                - Most plots assume at least 2D components or features for visualization.
            """

        self._data = data
        self._components = components
        self._explained_inertia = explained_inertia
        self._clusters = clusters

    @property
    def data(self) -> pd.DataFrame:
        """Returns the data used for visualization."""
        return self._data

    @property
    def components(self) -> Optional[np.ndarray]:
        """Returns the matrix of principal components."""
        return self._components

    @property
    def explained_inertia(self) -> float:
        """Returns the explained inertia percentage."""
        return self._explained_inertia

    @property
    def clusters(self) -> Optional[np.ndarray]:
        """Returns the cluster labels for each data point."""
        return self._clusters

    def plot_principal_plane(self, title: str = "") -> None:
        """
        Generates a plot of the principal plane using the principal components.

        Parameters:
            title (str, optional): Custom title to add above the default title.
        """
        default_title = "Principal Plane"
        if title:
            full_title = f"{title}\n{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        else:
            full_title = f"{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        # Assumes self.components is a numpy array with at least 2 columns.
        x, y = self.components[:, 0], self.components[:, 1]
        plt.scatter(x, y, color="gray")
        # Use the data index for labels.
        for i, label in enumerate(self.data.index):
            plt.text(x[i], y[i], label, fontsize=9, ha="right")
        plt.title(full_title)
        plt.axhline(y=0, color="dimgrey", linestyle="--")
        plt.axvline(x=0, color="dimgrey", linestyle="--")
        plt.xlabel("Component 1")
        plt.ylabel("Component 2")
        plt.show()

    def plot_principal_plane_with_clusters(self, title: str = "") -> None:
        """
        Generates a plot of the principal plane with points colored according to clusters.

        Parameters:
            title (str, optional): Custom title to add above the default title.

        Raises:
            ValueError: If cluster information is not provided.
        """
        if self.clusters is None:
            raise ValueError("Cluster information is required for this plot.")
        default_title = "Principal Plane With Clusters"
        if title:
            full_title = f"{title}\n{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        else:
            full_title = f"{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        x, y = self.components[:, 0], self.components[:, 1]
        plt.figure(figsize=(10, 8))
        unique_clusters = np.unique(self.clusters)
        for cluster in unique_clusters:
            cluster_points = self.clusters == cluster
            plt.scatter(x[cluster_points], y[cluster_points], label=f"Cluster {cluster}", alpha=0.7)
        for i, label in enumerate(self.data.index):
            plt.text(x[i], y[i], label, fontsize=8, ha="right")
        plt.title(full_title)
        plt.axhline(y=0, color="dimgrey", linestyle="--")
        plt.axvline(x=0, color="dimgrey", linestyle="--")
        plt.xlabel("Component 1")
        plt.ylabel("Component 2")
        plt.legend()
        plt.show()

    def plot_correlation_circle(self, correlations: pd.DataFrame, title: str = "", scale: float = 1,
                                draw_circle: bool = True) -> None:
        """
        Generates a correlation circle for the principal components.

        Parameters:
            correlations (pandas.DataFrame): DataFrame containing the correlations for each variable.
            title (str, optional): Custom title to add above the default title.
            scale (float, optional): Scaling factor for the arrows. Defaults to 1.
            draw_circle (bool, optional): Whether to draw the unit circle. Defaults to True.
        """
        default_title = "Correlation Circle"
        if title:
            full_title = f"{title}\n{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        else:
            full_title = f"{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        if draw_circle:
            circle = plt.Circle((0, 0), radius=1.05, color="steelblue", fill=False)
            plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.axhline(y=0, color="dimgrey", linestyle="--")
        plt.axvline(x=0, color="dimgrey", linestyle="--")
        for i in range(correlations.shape[0]):
            plt.arrow(0, 0, correlations.iloc[i, 0] * scale, correlations.iloc[i, 1] * scale,
                      color="steelblue", alpha=0.5, head_width=0.05, head_length=0.05)
            plt.text(correlations.iloc[i, 0] * scale, correlations.iloc[i, 1] * scale,
                     self.data.columns[i], fontsize=9, ha="right")
        plt.title(full_title)
        plt.show()

    def plot_2d_scatter_with_clusters(self, x_col: str, y_col: str, cluster_col: str,
                                      title: str = "", figsize: Tuple[int, int] = (10, 8)) -> None:
        """
        Generates a 2D scatter plot colored by cluster.

        Parameters:
            x_col (str): Name of the column for the x-axis.
            y_col (str): Name of the column for the y-axis.
            cluster_col (str): Name of the column containing cluster labels.
            title (str, optional): Custom title to add above the default title.
            figsize (tuple, optional): Figure size. Defaults to (10, 8).
        """
        default_title = "2D Cluster Projection – Visualization of Groupings"
        if title:
            full_title = f"{title}\n{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        else:
            full_title = f"{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        plt.figure(figsize=figsize)
        unique_clusters = np.unique(self.data[cluster_col])
        for cluster in unique_clusters:
            subset = self.data[self.data[cluster_col] == cluster]
            plt.scatter(subset[x_col], subset[y_col], label=f"Cluster {cluster}", s=20, edgecolor="k")
        plt.title(full_title)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.axis("equal")
        plt.legend(title="Clusters", loc="best", bbox_to_anchor=(1.05, 1))
        plt.tight_layout()
        plt.show()

    def plot_3d_scatter_with_clusters(self, x_col: str, y_col: str, z_col: str, cluster_col: str,
                                      title: str = "", figsize: Tuple[int, int] = (12, 8),
                                      cmap: str = "viridis", s: int = 50, alpha: float = 0.7) -> None:
        """
        Creates a 3D scatter plot colored by cluster.

        Parameters:
            x_col (str): Name of the column for the x-axis.
            y_col (str): Name of the column for the y-axis.
            z_col (str): Name of the column for the z-axis.
            cluster_col (str): Name of the column containing cluster labels.
            title (str, optional): Custom title to add above the default title.
            figsize (tuple, optional): Figure size. Defaults to (12, 8).
            cmap (str, optional): Colormap to use. Defaults to "viridis".
            s (int, optional): Size of the points. Defaults to 50.
            alpha (float, optional): Transparency of the points. Defaults to 0.7.
        """
        default_title = "3D Scatter Plot – Cluster Distribution"
        if title:
            full_title = f"{title}\n{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"
        else:
            full_title = f"{default_title} (Explained Inertia: {self.explained_inertia:.2f}%)"

        cluster_codes, unique_clusters = pd.factorize(self.data[cluster_col])

        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, projection="3d")
        scatter = ax.scatter(self.data[x_col], self.data[y_col], self.data[z_col],
                             c=cluster_codes, cmap=cmap, s=s, alpha=alpha)

        for i, cluster_name in enumerate(unique_clusters):
            color = plt.cm.get_cmap(cmap)(scatter.norm(i))
            ax.scatter([], [], [], color=color, label=f"Cluster {cluster_name}")
        ax.set_title(full_title)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_zlabel(z_col)
        ax.legend(title="Clusters", loc="upper left", bbox_to_anchor=(1, 0.8))
        plt.tight_layout()
        plt.show()
