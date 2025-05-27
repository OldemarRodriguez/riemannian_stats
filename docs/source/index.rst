.. image:: _static/images/logo.jpg
   :alt: RiemannianStats
   :width: 500px
   :align: center


Riemannian STATS
================

**Riemannian STATS: Statistical Analysis on Riemannian Manifolds**

**Riemannian STATS** is an open-source package that implements a novel principal component analysis methodology adapted for data on Riemannian manifolds, using UMAP as a core tool to construct the underlying geometric structure. This tool enables advanced statistical techniques to be applied to any type of dataset, honoring its local geometry, without requiring the data to originate from traditionally geometric domains like medical imaging or shape analysis.

Instead of assuming data resides in Euclidean space, RiemannianStats transforms any data table into a Riemannian manifold by leveraging the local connectivity extracted from a UMAP-generated k-nearest neighbor graph. On top of this structure, the package computes Riemannian principal components, covariance and correlation matrices, and even provides 2D and 3D visualizations that faithfully capture the dataset’s topology.

With **Riemannian STATS**, you can:

* Incorporate the local geometry of your data for meaningful dimensionality reduction.
* Generate visual representations that better reflect the true structure of your data.
* Use a unified framework that generalizes classical statistical analysis to complex geometric contexts.
* Apply these techniques to both synthetic and real high-dimensional datasets.

This package is ideal for researchers, data scientists, and developers seeking to move beyond the traditional assumptions of classical statistics, applying models that respect the intrinsic structure of data.

**User Guide**

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
           <span>Riemannian STATS Package</span>
       </a>
    <a href="github_repository.html" class="card">
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
      Install Riemannian STATS           <installation>
      RiemannianStats Package           <riemannian_stats>
      Source Code and Contributors      <github_repository>
      Scientific Paper                  <paper>
