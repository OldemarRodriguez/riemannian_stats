"""
Este script prueba que los atributos derivados en RiemannianUMAPAnalysis
se recalculan automáticamente al cambiar 'data' y 'n_neighbors'.

Se utilizan los datasets:
- Data10D_250.csv
- iris.csv
"""

from riemannian_stats import riemannian_analysis, data_processing, utilities

# ---------------------------
# Paso 1: Cargar primer dataset (Data10D_250.csv)
# ---------------------------
data_10d_full = data_processing.load_data(
    "./data/Data10D_250.csv", separator=",", decimal="."
)
if "cluster" in data_10d_full.columns:
    data_10d = data_10d_full.drop(columns=["cluster"])
else:
    data_10d = data_10d_full
n_neighbors_10d = int(len(data_10d) / 5)

print("\n🔍 Inicializando análisis con Data10D_250.csv")
analysis = riemannian_analysis(data_10d, n_neighbors=n_neighbors_10d)

print("\n[ANTES de modificar data y n_neighbors]")
print("calculate_umap_graph_similarities:")
print(analysis.umap_similarities)

print("\ncalculate_rho_matrix:")
print(analysis.rho)

print("\nriemannian_vector_difference:")
print(analysis.riemannian_diff)

print("\ncalculate_umap_distance_matrix:")
print(analysis.umap_distance_matrix)

riemann_corr_10d = analysis.riemannian_correlation_matrix()
print("\nriemannian_correlation_matrix:")
print(riemann_corr_10d)

components_10d = analysis.riemannian_components_from_data_and_correlation(
    riemann_corr_10d
)
print("\nriemannian_components_from_data_and_correlation:")
print(components_10d)

inertia_10d = utilities.pca_inertia_by_components(riemann_corr_10d, 0, 1) * 100
print("\npca_inertia_by_components:")
print(inertia_10d)

correlations_10d = analysis.riemannian_correlation_variables_components(components_10d)
print("\nriemannian_correlation_variables_components:")
print(correlations_10d)

# ---------------------------
# Paso 2: Cargar segundo dataset (iris.csv) y modificar analysis.data
# ---------------------------
iris_full = data_processing.load_data("./data/iris.csv", separator=";", decimal=".")
if "tipo" in iris_full.columns:
    iris_data = iris_full.drop(columns=["tipo"])
else:
    iris_data = iris_full

n_neighbors_iris = int(len(iris_data) / 3)

# Reasignar datos y n_neighbors → debería forzar recálculo
print("\n🔁 Reasignando analysis.data y analysis.n_neighbors con datos de iris.csv")
analysis.data = iris_data
analysis.n_neighbors = n_neighbors_iris

print("\n[DESPUÉS de modificar data y n_neighbors]")
print("calculate_umap_graph_similarities:")
print(analysis.umap_similarities)

print("\ncalculate_rho_matrix:")
print(analysis.rho)

print("\nriemannian_vector_difference:")
print(analysis.riemannian_diff)

print("\ncalculate_umap_distance_matrix:")
print(analysis.umap_distance_matrix)

riemann_corr_iris = analysis.riemannian_correlation_matrix()
print("\nriemannian_correlation_matrix:")
print(riemann_corr_iris)

components_iris = analysis.riemannian_components_from_data_and_correlation(
    riemann_corr_iris
)
print("\nriemannian_components_from_data_and_correlation:")
print(components_iris)

inertia_iris = utilities.pca_inertia_by_components(riemann_corr_iris, 0, 1) * 100
print("\npca_inertia_by_components:")
print(inertia_iris)

correlations_iris = analysis.riemannian_correlation_variables_components(
    components_iris
)
print("\nriemannian_correlation_variables_components:")
print(correlations_iris)
