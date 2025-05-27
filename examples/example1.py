"""
This script demonstrates a comprehensive workflow for analyzing a high-dimensional dataset (Data10D_250.csv)
using the riemannian_stats package. Initially, the dataset is loaded and preprocessed using data_processing.load_data(),
with a comma as the separator and a dot as the decimal marker. The script verifies the presence of a 'cluster' column
to extract clustering information and separates it from the data used for analysis, preserving a copy of the original
dataset for visualization purposes.

Next, an instance of riemannian_analysis is created to compute several key metrics including:
- UMAP graph similarities,
- The rho matrix,
- Riemannian vector differences,
- The UMAP distance matrix,
- Riemannian covariance and correlation matrices.

Following this, the script extracts the principal components from the correlation matrix and calculates the explained
inertia using the first two components. It also computes correlations between the original variables and these components.

Finally, a suite of visualizations is generated based on the availability of clustering information. These include:
- A 2D scatter plot with clusters,
- A principal plane plot with clusters,
- A 3D scatter plot with clusters,
- A correlation circle plot.

This example illustrates how riemannian_stats enables a thorough analysis of complex high-dimensional data,
effectively extracting and visually representing its key features in Riemannian spaces.
"""

from riemannian_stats import riemannian_analysis, visualization, data_processing, utilities

# ---------------------------
# Example 3: Data10D_250 Dataset
# ---------------------------
# Load the Data10D_250.csv dataset using data_processing.load_data, specifying the separator and decimal format.
data = data_processing.load_data("./data/Data10D_250.csv", separator=",", decimal=".")

# TODO: CAMBIAR data_processing POR pandas
# Para importar el archivo tanbien puedes usar la libreria de pandas de la siguiente forma:
# import pandas as pd
# df = pd.read_csv("./data/Data10D_250.csv", sep=",", decimal="." )

# Define the number of neighbors as the length of the data divided by the number of clusters (in this example, 5).
n_neighbors = int(len(data) / 5)

# Check if the 'cluster' column exists to identify groups (clusters).
if 'cluster' in data.columns:
    clusters = data['cluster']
    data_with_clusters = data.copy()
    data = data.iloc[:, :-1]
else:
    clusters = None
    data_with_clusters = data

# Create an instance of Riemannian analysis for the dataset.
analysis = riemannian_analysis(data, n_neighbors=n_neighbors)

# --------------------------------------------------------
# Compute UMAP graph similarities and the rho matrix for the data.
# --------------------------------------------------------
umap_similarities = analysis.umap_similarities
print("calculate_umap_graph_similarities:", umap_similarities)

rho = analysis.rho
print("calculate_rho_matrix:", rho)

# --------------------------------------------------------
# Compute Riemannian vector differences and the UMAP distance matrix.
# --------------------------------------------------------
riemannian_diff = analysis.riemannian_diff
print("riemannian_vector_difference:", riemannian_diff)

umap_distance_matrix = analysis.umap_distance_matrix
print("calculate_umap_distance_matrix:", umap_distance_matrix)

# --------------------------------------------------------
# Compute the Riemannian correlation matrices, and extract principal components.
# --------------------------------------------------------
riemann_corr = analysis.riemannian_correlation_matrix()
print("riemannian_correlation_matrix:", riemann_corr)

riemann_components = analysis.riemannian_components_from_data_and_correlation(riemann_corr)
print("riemannian_components_from_data_and_correlation:", riemann_components)

# --------------------------------------------------------
# Compute the explained inertia (using components 0 and 1).
# --------------------------------------------------------
comp1, comp2 = 0, 1
inertia = utilities.pca_inertia_by_components(riemann_corr, comp1, comp2) * 100
print("pca_inertia_by_components:", inertia)

# --------------------------------------------------------
# Compute correlations between original variables and the first two principal components.
# --------------------------------------------------------
correlations = analysis.riemannian_correlation_variables_components(riemann_components)
print("riemannian_correlation_variables_components:", correlations)

# --------------------------------------------------------
# Visualization: Create plots based on the availability of clusters.
# If clusters are provided, use cluster-based plots; otherwise, use plots without clusters.
# --------------------------------------------------------
if clusters is not None:
    viz = visualization(data=data_with_clusters,
                        components=riemann_components,
                        explained_inertia=inertia,
                        clusters=clusters)
    try:
        viz.plot_2d_scatter_with_clusters(x_col="x", y_col="y", cluster_col="cluster", title="Data10D_250.csv")
    except Exception as e:
        print("2D scatter plot with clusters failed:", e)

    try:
        viz.plot_principal_plane_with_clusters(title="Data10D_250.csv")
    except Exception as e:
        print("Principal plane with clusters plot failed:", e)

    try:
        viz.plot_3d_scatter_with_clusters(x_col="x", y_col="y", z_col="var1", cluster_col="cluster",
                                          title="Data10D_250.csv", figsize=(12, 8))
    except Exception as e:
        print("3D scatter plot with clusters failed:", e)
else:
    viz = visualization(data=data,
                        components=riemann_components,
                        explained_inertia=inertia)
    try:
        viz.plot_principal_plane(title="Data10D_250.csv")
    except Exception as e:
        print("Principal plane plot failed:", e)

# Plot the correlation circle (works regardless of clusters).
try:
    viz.plot_correlation_circle(correlations=correlations, title="Data10D_250.csv")
except Exception as e:
    print("Correlation circle plot failed:", e)
