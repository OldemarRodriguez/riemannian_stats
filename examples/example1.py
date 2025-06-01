"""
This script demonstrates how to use the `riemannian_stats` package to perform a detailed
Riemannian analysis of the Iris dataset—a classic benchmark for multi-class classification.

The script begins by loading the Iris dataset and converting it into a pandas DataFrame.
It includes species labels as cluster identifiers (0: Setosa, 1: Versicolor, 2: Virginica).
The number of neighbors is automatically computed based on the number of samples per class.

An instance of RiemannianAnalysis is then initialized to compute:
- UMAP similarity matrix,
- Rho matrix (1 - similarity),
- Riemannian vector differences,
- UMAP distance matrix,
- Riemannian correlation matrix.

The script continues by extracting principal components and calculating the explained inertia
for the first two components. It also computes the correlations between the original variables
and the extracted components.

Finally, a set of visualizations is produced:
- 2D scatter plot with clusters,
- Principal plane with clusters,
- 3D scatter plot with clusters,
- Correlation circle.

This example shows how `riemannian_stats` enables robust exploration of structured numerical data
using Riemannian geometry and visual analysis techniques.
"""

from riemannian_stats import riemannian_analysis, visualization, utilities
import pandas as pd
from sklearn.datasets import load_iris

# ---------------------------
# Load the Iris dataset
# ---------------------------
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
clusters = pd.Series(iris.target)  # Species labels: 0, 1, 2

# Define number of neighbors based on samples per class (150 / 3)
n_neighbors = int(len(data) / 3)

# ---------------------------
# Initialize Riemannian analysis
# ---------------------------
analysis = riemannian_analysis(data, n_neighbors=n_neighbors)

# ---------------------------
# Compute Riemannian matrices
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
# Correlation matrix and PCA
# ---------------------------
riemann_corr = analysis.riemannian_correlation_matrix()
print("Riemannian Correlation Matrix:", riemann_corr)

riemann_components = analysis.riemannian_components_from_data_and_correlation(riemann_corr)
print("Principal Components:", riemann_components)

# ---------------------------
# Explained inertia and feature correlations
# ---------------------------
comp1, comp2 = 0, 1
inertia = utilities.pca_inertia_by_components(riemann_corr, comp1, comp2) * 100
print("Explained Inertia (%):", inertia)

correlations = analysis.riemannian_correlation_variables_components(riemann_components)
print("Variable-Component Correlations:", correlations)

# ---------------------------
# Prepare data for visualization
# ---------------------------
data_with_clusters = data.copy()
data_with_clusters['x'] = riemann_components[:, 0]
data_with_clusters['y'] = riemann_components[:, 1]
data_with_clusters['var1'] = riemann_components[:, 2] if riemann_components.shape[1] > 2 else 0
data_with_clusters['cluster'] = clusters

# ---------------------------
# Generate visualizations
# ---------------------------
viz = visualization(data=data_with_clusters,
                    components=riemann_components,
                    explained_inertia=inertia,
                    clusters=clusters)

try:
    viz.plot_2d_scatter_with_clusters(x_col="x", y_col="y", cluster_col="cluster", title="Iris Dataset")
except Exception as e:
    print("2D Scatter Plot Failed:", e)

try:
    viz.plot_principal_plane_with_clusters(title="Iris Dataset")
except Exception as e:
    print("Principal Plane Plot Failed:", e)

try:
    viz.plot_3d_scatter_with_clusters(x_col="x", y_col="y", z_col="var1", cluster_col="cluster",
                                      title="Iris Dataset", figsize=(12, 8))
except Exception as e:
    print("3D Scatter Plot Failed:", e)

try:
    viz.plot_correlation_circle(correlations=correlations, title="Iris Dataset")
except Exception as e:
    print("Correlation Circle Plot Failed:", e)
