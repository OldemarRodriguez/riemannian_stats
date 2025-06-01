"""
This script demonstrates how to use the `riemannian_stats` package to perform a comprehensive
analysis of high-dimensional face data using the Olivetti Faces dataset from sklearn.

The script begins by loading the Olivetti Faces dataset and converting it into a pandas DataFrame.
It also extracts cluster labels representing individual identities (0 to 39), which can be used
for visualization purposes. The number of neighbors for UMAP is dynamically determined as the number
of samples per person in the dataset.

An instance of `RiemannianAnalysis` is then created to perform the following computations:
- UMAP similarity matrix,
- Rho matrix (1 - similarity),
- Riemannian vector differences,
- UMAP distance matrix,
- Riemannian correlation matrix.

It continues by extracting principal components from the correlation matrix, calculating the explained
inertia for the first two components, and computing correlations between original features and components.

Finally, the script generates visualizations, including:
- 2D and 3D scatter plots by clusters (identities),
- Principal plane with clusters,
- Correlation circle.

This example illustrates the capabilities of `riemannian_stats` to explore complex image datasets
in a Riemannian framework.
"""

from riemannian_stats import riemannian_analysis, visualization, utilities
import pandas as pd
from sklearn.datasets import fetch_olivetti_faces

# ---------------------------
# Load the Olivetti Faces dataset
# ---------------------------
# Load the Olivetti Faces dataset using pd.DataFrame
faces = fetch_olivetti_faces(shuffle=True, random_state=42)
data = pd.DataFrame(faces.data)
clusters = pd.Series(faces.target)
n_neighbors = int(len(data) / 40)

# ---------------------------
# Create Riemannian Analysis instance
# ---------------------------
analysis = riemannian_analysis(data, n_neighbors=n_neighbors)

# ---------------------------
# Riemannian metrics and matrices
# ---------------------------
umap_similarities = analysis.umap_similarities
print("UMAP Similarities Matrix:", umap_similarities)

rho = analysis.rho
print("Rho Matrix:", rho)

riemannian_diff = analysis.riemannian_diff
print("Riemannian Vector Differences:", riemannian_diff)

umap_distance_matrix = analysis.umap_distance_matrix
print("UMAP Distance Matrix:", umap_distance_matrix)

# ---------------------------
# Correlation and PCA
# ---------------------------
riemann_corr = analysis.riemannian_correlation_matrix()
print("Riemannian Correlation Matrix:", riemann_corr)

riemann_components = analysis.riemannian_components_from_data_and_correlation(riemann_corr)
print("Riemannian Components:", riemann_components)

# ---------------------------
# Explained inertia and correlations
# ---------------------------
comp1, comp2 = 0, 1
inertia = utilities.pca_inertia_by_components(riemann_corr, comp1, comp2) * 100
print("Explained Inertia (%):", inertia)

correlations = analysis.riemannian_correlation_variables_components(riemann_components)
print("Variable-Component Correlations:", correlations)

# ---------------------------
# Visualization
# ---------------------------
# Add components and cluster for 2D/3D plotting
data_with_clusters = data.copy()
data_with_clusters['x'] = riemann_components[:, 0]
data_with_clusters['y'] = riemann_components[:, 1]
data_with_clusters['var1'] = riemann_components[:, 2] if riemann_components.shape[1] > 2 else 0
data_with_clusters['cluster'] = clusters

viz = visualization(data=data_with_clusters,
                    components=riemann_components,
                    explained_inertia=inertia,
                    clusters=clusters)

try:
    viz.plot_2d_scatter_with_clusters(x_col="x", y_col="y", cluster_col="cluster", title="Olivetti Faces")
except Exception as e:
    print("2D Scatter Plot Failed:", e)

try:
    viz.plot_principal_plane_with_clusters(title="Olivetti Faces")
except Exception as e:
    print("Principal Plane Plot Failed:", e)

try:
    viz.plot_3d_scatter_with_clusters(x_col="x", y_col="y", z_col="var1", cluster_col="cluster",
                                      title="Olivetti Faces", figsize=(12, 8))
except Exception as e:
    print("3D Scatter Plot Failed:", e)

try:
    viz.plot_correlation_circle(correlations=correlations, title="Olivetti Faces")
except Exception as e:
    print("Correlation Circle Plot Failed:", e)
