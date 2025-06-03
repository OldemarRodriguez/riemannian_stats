"""
This script demonstrates a complete workflow for analyzing the classic Iris dataset (iris.csv)
using the riemannian_stats package. The dataset is loaded and preprocessed using pd.read_csv(),
with a semicolon as the separator and a dot as the decimal marker. The script checks for the presence
of a 'tipo' column to extract clustering information and separates it from the main analysis data.

Next, an instance of riemannian_analysis is created to compute several key metrics including:
- UMAP graph similarities,
- The rho matrix,
- Riemannian vector differences,
- The UMAP distance matrix,
- Riemannian covariance and correlation matrices.

Principal components are extracted from the correlation matrix, and the explained inertia (using the first two
components) is calculated as a percentage. Additionally, correlations between the original variables and the first
two principal components are computed.

Finally, the script generates various visualizations depending on whether clustering information is available:
- A 2D scatter plot with clusters,
- A principal plane plot with clusters,
- A 3D scatter plot with clusters,
- And a correlation circle plot.

This example illustrates the flexibility of riemannian_stats in handling a classical, lower-dimensional dataset
with clusters, enabling a comprehensive visual exploration of the data.
"""

from riemannian_stats import riemannian_analysis, visualization, utilities
import pandas as pd

# ---------------------------
# Example 2: Iris Dataset
# ---------------------------
# Load the iris.csv dataset using pd.read_csv, specifying the separator and decimal format.
data = pd.read_csv("./data/iris.csv", sep=";", decimal=".")

# Define the number of neighbors as the length of the data divided by the number of clusters (in this example, 3).
n_neighbors = int(len(data) / 3)

# Check if the 'species' column exists to identify groups (clusters).
if "species" in data.columns:
    clusters = data["species"]
    # Keep a copy of the original DataFrame (with the 'species' column) for 2D and 3D visualizations.
    data_with_clusters = data.copy()
    # Remove the 'species' column from the data for analysis (if needed).
    data = data.iloc[:, :-1]
else:
    clusters = None
    data_with_clusters = data

# Create an instance of RiemannianUMAPAnalysis for the dataset.
analysis = riemannian_analysis(data, n_neighbors=n_neighbors)

# --------------------------------------------------------
# Compute UMAP graph similarities and the rho matrix for the data.
# --------------------------------------------------------
umap_similarities = analysis.umap_similarities
print("UMAP Similarities Matrix:", umap_similarities)

rho = analysis.rho
print("Rho Matrix:", rho)

# --------------------------------------------------------
# Compute Riemannian vector differences and the UMAP distance matrix.
# --------------------------------------------------------
riemannian_diff = analysis.riemannian_diff
print("Riemannian Vector Differences:", riemannian_diff)

umap_distance_matrix = analysis.umap_distance_matrix
print("UMAP Distance Matrix:", umap_distance_matrix)

# --------------------------------------------------------
# Compute the Riemannian correlation matrices, and extract principal components.
# --------------------------------------------------------
riemann_corr = analysis.riemannian_correlation_matrix()
print("Riemannian Correlation Matrix:", riemann_corr)

riemann_components = analysis.riemannian_components_from_data_and_correlation(
    riemann_corr
)
print("Riemannian Components:", riemann_components)

# --------------------------------------------------------
# Compute the explained inertia (using components 0 and 1) as a percentage.
# --------------------------------------------------------
comp1, comp2 = 0, 1
inertia = utilities.pca_inertia_by_components(riemann_corr, comp1, comp2) * 100
print("Explained Inertia (%):", inertia)

# --------------------------------------------------------
# Compute correlations between the original variables and the first two principal components.
# --------------------------------------------------------
correlations = analysis.riemannian_correlation_variables_components(riemann_components)
print("Variable-Component Correlations:", correlations)

# --------------------------------------------------------
# Visualization: Create plots based on the availability of clusters.
# If clusters are provided, use cluster-based plots; otherwise, use plots without clusters.
# --------------------------------------------------------
if clusters is not None:
    # Create a Visualization instance including cluster information.
    viz = visualization(
        data=data_with_clusters,
        components=riemann_components,
        explained_inertia=inertia,
        clusters=clusters,
    )
    try:
        # 1. 2D scatter plot with clusters (requires the 'species' column in the DataFrame).
        viz.plot_2d_scatter_with_clusters(
            x_col="sepal.length",
            y_col="sepal.width",
            cluster_col="species",
            title="iris.csv",
        )
    except Exception as e:
        print("2D scatter plot with clusters failed:", e)

    try:
        # 2. Principal plane plot with clusters.
        viz.plot_principal_plane_with_clusters(title="iris.csv")
    except Exception as e:
        print("Principal plane with clusters plot failed:", e)

    try:
        # 3. 3D scatter plot with clusters (requires the 'species' column and appropriate 3D data columns).
        viz.plot_3d_scatter_with_clusters(
            x_col="sepal.length",
            y_col="sepal.width",
            z_col="petal.length",
            cluster_col="species",
            title="iris.csv",
            figsize=(12, 8),
        )
    except Exception as e:
        print("3D scatter plot with clusters failed:", e)
else:
    # Create a Visualization instance without clusters.
    viz = visualization(
        data=data, components=riemann_components, explained_inertia=inertia
    )
    try:
        # Plot the principal plane (does not require cluster information).
        viz.plot_principal_plane(title="iris.csv")
    except Exception as e:
        print("Principal plane plot failed:", e)

# 4. Plot the correlation circle (should work regardless of clusters).
try:
    viz.plot_correlation_circle(correlations=correlations, title="iris.csv")
except Exception as e:
    print("Correlation circle plot failed:", e)
