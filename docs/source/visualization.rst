Module Details
==============

The ``Visualization`` class provides a collection of plotting tools tailored to dimensionality reduction results such as PCA or UMAP. It helps reveal data structures, clusters, and relationships between variables through intuitive 2D and 3D visualizations.

Overview
--------

This module is designed to make sense of high-dimensional data by projecting it into interpretable low-dimensional spaces and offering multiple visualization options. It enables analysis of principal components, cluster distributions, and variable relationships through correlation plots.

Key Capabilities
----------------

- **Principal Plane Visualization**: Display a 2D projection of the first two components, with or without cluster labels.
- **Correlation Circle Plot**: Analyze how original variables relate to principal components.
- **2D Cluster Scatter Plot**: Quickly visualize cluster distributions in two selected dimensions.
- **3D Cluster Scatter Plot**: Explore spatial groupings of data points in three dimensions with optional customization.

Use Cases
---------

Use the ``Visualization`` module when:

- You want to interpret results from PCA, UMAP, or any other dimensionality reduction method.
- You need to visualize how data clusters or groups behave in reduced space.
- You want to analyze relationships between variables and components using intuitive plots.

Usage Example
-------------

Below is a minimal example of how to use the ``Visualization`` class. It assumes you have already computed principal components and optionally cluster labels:

.. code-block:: python

   import pandas as pd
   import numpy as np
   from riemannian_stats.visualization import Visualization

   # Load data (you can use a processed dataset or raw input)
   df = pd.read_csv("path/to/data.csv", sep=",", decimal=".")

   # Dummy principal components (e.g., from PCA or UMAP)
   components = np.random.rand(len(df), 2)

   # Optional cluster labels
   clusters = df["cluster"].values if "cluster" in df.columns else None

   # Initialize the visualization object
   viz = Visualization(data=df, components=components, explained_inertia=78.3, clusters=clusters)

   # Plot the principal plane
   viz.plot_principal_plane_with_clusters(title="Sample Data")

For comprehensive usage examples with real datasets, refer to the **"How to Use Riemannian STATS"** section, available both on the homepage (index) and in the sidebar navigation of the documentation.

API Documentation
--------------------

.. autoclass:: riemannian_stats.visualization.Visualization
   :members:
   :undoc-members:
   :show-inheritance:
