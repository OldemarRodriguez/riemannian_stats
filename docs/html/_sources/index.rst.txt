.. image:: _static/images/logo.jpg
   :alt: RiemannianStats
   :width: 500px
   :align: center

Riemannian STATS
================

**Riemannian STATS: Statistical Analysis on Riemannian Manifolds**

**Riemannian STATS** is a Python package designed to extend classical multivariate statistical methods to data that lie on non-Euclidean spaces. This package introduces a general framework for **Riemannian Principal Component Analysis (R-PCA)**, a method developed to operate on datasets modeled as **Riemannian manifolds**. The foundational ideas are presented in the scientific paper `"Riemannian Principal Component Analysis"` by Oldemar Rodríguez.

Unlike traditional PCA, which assumes a flat Euclidean geometry, R-PCA uses **UMAP** to define local distances and induce a Riemannian structure from any data table—structured or unstructured, real or synthetic. This enables geometric-aware dimensionality reduction and correlation analysis, even on datasets with complex topologies, non-linear relationships, or varying local densities.

Built on these principles, **Riemannian STATS** enables:

- Transformation of data tables into Riemannian manifolds via UMAP-based metrics.
- Riemannian correlation and covariance computation.
- Extraction of Riemannian principal components.
- Intuitive 2D/3D visualizations reflecting the manifold’s geometry.
- Applications in high-dimensional data, image analysis, clustering, and beyond.

The core idea is simple yet powerful: **treat your dataset not as flat, but as curved**—honoring its internal structure. This unlocks more expressive models, better visualizations, and more accurate statistical summaries.

**Ideal for** researchers, data scientists, and developers looking to enhance their analysis of complex datasets with geometry-aware tools.

**You can install Riemannian STATS directly from PyPI:** `Riemannian STATS on PyPI <https://pypi.org/project/riemannian-stats/0.1.0/>`_

**User Guide**
--------------

.. raw:: html

   <div class="card-grid">
       <a href="examples.html" class="card">
           <img src="_static/icons/example.svg" alt="Examples">
           <span>How to Use Riemannian STATS</span>
       </a>
       <a href="installation.html" class="card">
           <img src="_static/icons/installation.png" alt="Installation">
           <span>Install Riemannian STATS</span>
       </a>
       <a href="riemannian_stats.html" class="card">
           <img src="_static/icons/package.png" alt="Riemannian STATS">
           <span>Riemannian STATS Modules</span>
       </a>
       <a href="contributing.html" class="card">
           <img src="_static/icons/github.png" alt="Source Code and Contributors">
           <span>Source Code and Contributors</span>
       </a>
       <a href="paper.html" class="card">
           <img src="_static/icons/paper.png" alt="Paper">
           <span>Scientific Paper</span>
       </a>
   </div>

.. only:: html

   .. toctree::
      :hidden:
      :maxdepth: 1

      How to Use Riemannian STATS       <examples>
      Install Riemannian STATS          <installation>
      RiemannianStats Modules           <riemannian_stats>
      Source Code and Contributors      <contributing>
      Scientific Paper                  <paper>
