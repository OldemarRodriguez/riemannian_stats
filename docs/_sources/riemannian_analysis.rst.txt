RiemannianAnalysis Module Details
=================================

The ``RiemannianAnalysis`` class combines the power of Uniform Manifold Approximation and Projection (UMAP) with Riemannian geometry, enabling a more insightful exploration of high-dimensional data.

Overview
--------

This module extends UMAP by incorporating Riemannian-based weighting to better capture the intrinsic geometry of the data. It enables more meaningful representations, particularly in contexts where non-Euclidean distance structures are important.

Key Capabilities
----------------

- **UMAP Dimensionality Reduction**: Applies UMAP for nonlinear dimensionality reduction with customizable parameters.
- **Riemannian Distance Weighting**: Integrates Riemannian weights to enhance pairwise similarity computation.
- **Custom Covariance and Correlation**: Computes covariance and correlation matrices adapted to the Riemannian structure of the dataset.
- **Riemannian PCA**: Performs principal component analysis using geometry-aware transformations.
- **Correlation with Components**: Computes variable-to-component correlations in Riemannian space.

Use Cases
---------

This module is especially useful in the following scenarios:

- High-dimensional datasets where traditional methods fail to capture intrinsic structures.
- Applications in neuroscience, biomechanics, and other fields that benefit from non-Euclidean analysis.
- Scenarios requiring geometry-informed PCA and correlation analysis.

Usage Example
-------------

Here's a simple example to demonstrate how to use the ``RiemannianAnalysis`` class with a dataset loaded using pandas:

.. code-block:: python

   import pandas as pd
   from riemannian_stats.riemannian_analysis import RiemannianAnalysis

   # Load your high-dimensional dataset
   df = pd.read_csv("path/to/data.csv", sep=",", decimal=".")

   # Create an analysis instance
   analysis = RiemannianAnalysis(df, n_neighbors=5, min_dist=0.1, metric="euclidean")

   # Compute the Riemannian correlation matrix
   corr_matrix = analysis.riemannian_correlation_matrix()

   # Extract principal components using the correlation matrix
   components = analysis.riemannian_components_from_data_and_correlation(corr_matrix)

   # Optionally, compute variable-component correlations
   variable_corr = analysis.riemannian_correlation_variables_components(components)

For full usage examples and real-world datasets, refer to the "How to Use Riemannian STATS" section, available both on the homepage (Home) and in the sidebar navigation.


API Documentation
-----------------

.. autoclass:: riemannian_stats.riemannian_analysis.RiemannianAnalysis
   :members:
   :undoc-members:
   :show-inheritance:
