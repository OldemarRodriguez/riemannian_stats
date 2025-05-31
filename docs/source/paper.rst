Scientific Paper
================

This section highlights the scientific foundation behind the **Riemannian STATS** package.

Riemannian Principal Component Analysis
---------------------------------------

**R-PCA** is a novel extension of Principal Component Analysis designed to operate on datasets that reside on
non-Euclidean spaces. Instead of assuming a flat Euclidean structure, R-PCA leverages local geometric information,
derived via the **UMAP** algorithm, to define a **Riemannian manifold** over the data. This allows for more accurate
dimensionality reduction and statistical analysis that respects the intrinsic structure of complex datasets.

**Applications include**:

- High-dimensional structured data
- Clustering with geometric consistency
- Real-world datasets such as image sets (e.g., Olivetti Faces)

R-PCA improves interpretability, variance capture, and clustering performance compared to standard
PCA especially in cases where local metrics vary significantly across the dataset.

📄 `Link to the complete paper: "Riemannian Principal Component Analysis" <_static/papers/RiemannianPCA_OldemarRodriguez.pdf>`_


.. raw:: html

    <div style="text-align:center; margin: 1.5em 0;">
        <iframe width="560" height="315"
                src="https://www.youtube.com/embed/MLAVRK_lGKs"
                title="R-PCA Presentation"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
        </iframe>
        <p style="font-style: italic; font-size: 90%;">Watch the official presentation introducing the concepts behind R-PCA. <strong>(Video in Spanish)</strong></p>
    </div>

