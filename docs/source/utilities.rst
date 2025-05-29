Utilities Module Details
========================

The ``Utilities`` module offers standalone helper functions for common analytical tasks, particularly useful in dimensionality reduction workflows such as PCA. It is designed for convenience—methods can be used directly without instantiating a class, making it ideal for fast integration into data pipelines.

Overview
--------

This module provides general-purpose mathematical tools, with a focus on principal component analysis. Its static design simplifies its use across scripts and notebooks without requiring object creation, helping streamline repetitive calculations like inertia evaluation.

Key Capabilities
----------------

- **Inertia Calculation for PCA**: Quickly compute the proportion of variance explained by two selected principal components of a correlation matrix.
- **Plug-and-Play Design**: Static methods that can be called directly from the class, enhancing usability across different modules and analyses.

Use Cases
---------

This module is especially useful when:

- You need to assess the explanatory power of selected PCA components.
- You want lightweight, dependency-free tools for inclusion in your custom data science workflows.
- You prefer quick function calls without having to manage object state or internal attributes.

Usage Example
-------------

Here’s a simple example of how to use the ``Utilities`` module:

.. code-block:: python

   import numpy as np
   from riemannian_stats.utilities import Utilities

   # Sample correlation matrix (symmetric and positive semi-definite)
   corr_matrix = np.array([[1.0, 0.8], [0.8, 1.0]])

   # Compute explained variance (inertia) by the first two components
   inertia = Utilities.pca_inertia_by_components(corr_matrix, component1=0, component2=1)

   print(f"Inertia explained by components 0 and 1: {inertia:.4f}")

For extended examples using this function within full analysis pipelines, refer to the **"How to Use Riemannian STATS"** section, accessible from both the homepage (index) and the sidebar of the documentation.

API Documentation
--------------------

.. autoclass:: riemannian_stats.utilities.Utilities
   :members:
   :undoc-members:
   :show-inheritance:
