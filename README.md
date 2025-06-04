<p align="center">
  <img src="https://github.com/OldemarRodriguez/riemannian_stats/raw/main/docs/source/_static/images/logo.jpg" alt="Logo" width="600"/>
</p>

<p align="center">
  <a href="https://pypi.org/project/riemannian-stats/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/riemannian-stats?color=brightgreen&label=PyPI&logo=pypi">
  </a>
  <a href="https://opensource.org/licenses/BSD-3-Clause">
    <img alt="License" src="https://img.shields.io/badge/license-BSD%203--Clause-blue.svg?logo=open-source-initiative">
  </a>
  <a href="https://riemannianstats.web.app/installation.html">
    <img alt="Install" src="https://img.shields.io/badge/install-guide-success?logo=python">
  </a>
  <a href="https://riemannianstats.web.app/examples.html">
    <img alt="Examples" src="https://img.shields.io/badge/examples-available-informational?logo=jupyter">
  </a>
  <a href="https://riemannianstats.web.app/riemannian_stats.html">
    <img alt="Docs" src="https://img.shields.io/badge/docs-full-orange?logo=readthedocs">
  </a>
  <a href="https://riemannianstats.web.app/paper.html">
    <img alt="Scientific Paper" src="https://img.shields.io/badge/paper-published-lightgrey?logo=academia">
  </a>
  <a href="https://riemannianstats.web.app/contributing.html">
    <img alt="Contributors" src="https://img.shields.io/badge/contributors-and%20source-9cf?logo=github">
  </a>
  <a href="https://riemannianstats.web.app">
    <img alt="Website" src="https://img.shields.io/badge/website-online-blueviolet?logo=firefox-browser">
  </a>
</p>



## **Riemannian STATS: Statistical Analysis on Riemannian Manifolds**

---
**RiemannianStats** is an open-source package that implements a novel principal component analysis methodology adapted for data on Riemannian manifolds, using UMAP as a core tool to construct the underlying geometric structure. This tool enables advanced statistical techniques to be applied to any type of dataset, honoring its local geometry, without requiring the data to originate from traditionally geometric domains like medical imaging or shape analysis.

Instead of assuming data resides in Euclidean space, RiemannianStats transforms any data table into a Riemannian manifold by leveraging the local connectivity extracted from a UMAP-generated k-nearest neighbor graph. On top of this structure, the package computes Riemannian principal components, covariance and correlation matrices, and even provides 2D and 3D visualizations that faithfully capture the dataset’s topology.

With **Riemannian STATS**, you can:

* Incorporate the local geometry of your data for meaningful dimensionality reduction.
* Generate visual representations that better reflect the true structure of your data.
* Use a unified framework that generalizes classical statistical analysis to complex geometric contexts.
* Apply these techniques to both synthetic and real high-dimensional datasets.

This package is ideal for researchers, data scientists, and developers seeking to move beyond the traditional assumptions of classical statistics, applying models that respect the intrinsic structure of data.


### 🌐 Package Website

You can explore the **Riemannian STATS** package, its features, and interactive examples at:
🔗 [https://riemannianstats.web.app](https://riemannianstats.web.app)

---

## Features and Modules

| Functionality            | Module                  | Documentation                                           |
|--------------------------|-------------------------|---------------------------------------------------------|
| Data preprocessing       | `data_processing.py`    | [🔗 data_processing](https://riemannianstats.web.app/data_processing.html) |
| Riemannian analysis      | `riemannian_analysis.py`| [🔗 riemannian_analysis](https://riemannianstats.web.app/riemannian_analysis.html) |
| Visualizations (2D/3D)   | `visualization.py`      | [🔗 visualization](https://riemannianstats.web.app/visualization.html) |
| Utilities                | `utilities.py`          | [🔗 utilities](https://riemannianstats.web.app/utilities.html) |

---

## Package structure

The project structure is organized as follows:

```
riemannian_stats/
│
├── riemannian_stats/
│   ├── __init__.py                      # Makes package modules importable
│   ├── data_processing.py               # Classes for data loading and manipulation
│   ├── riemannian_analysis.py           # Riemannian statistical
│   ├── visualization.py                 # Functions and classes for result visualization
│   └── utilities.py                     # General utility functions
│
├── tests/                               # Unit tests for each module
│   ├── conftest.py
│   ├── test_riemannian_analysis.py
│   ├── test_visualization.py
│   └── test_utilities.py
│
├── docs/                                # Project documentation
│   └── ...
│
├── examples/                            # Examples demonstrating package usage
│   ├── data/
│       └── Data10D_250.cvs
│       └── iris.cvs
│   ├── example1.py
│   └── example2.py
│   └── example3.py
│
├── requirements.txt                     # Dependencies 
├── pyproject.toml                       # Package installation script
├── README.md                            # General information and usage of the package
└── LICENSE.txt                          # BSD-3-Clause License
```

---

---

### 📚 Examples of Use

The `examples/` directory contains three complete use cases applying Riemannian STATS to different datasets:

| Dataset        | Description                                                                                                                                                   | Script                                 | Results                                                                          |
| -------------- |---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------| -------------------------------------------------------------------------------- |
| Iris           | Applies Riemannian PCA to 150 flowers from 3 species using 4 morphological variables (sepal/petal length and width). Visualizes species in component space.   | [🧾 example1.py](examples/example1.py) | [📊 View Output](https://riemannianstats.web.app/_static/examples/Example1.html) |
| Data10D\_250   | Synthetic dataset with 250 points in 10 dimensions and labeled clusters. Computes UMAP similarities, rho matrix, R-PCA, and correlation analysis.             | [🧾 example2.py](examples/example2.py)          | [📊 View Output](https://riemannianstats.web.app/_static/examples/Example2.html) |
| Olivetti Faces | 400 grayscale face images (64×64 pixels, 4096D) from 40 individuals. Projects them into Riemannian component space for identity separation and visualization. | [🧾 example3.py](examples/example3.py)          | [📊 View Output](https://riemannianstats.web.app/_static/examples/Example3.html) |


📖 For full walkthroughs with inputs, outputs, and visualizations:
[📊 Examples Overview](https://riemannianstats.web.app/examples.html)

---

### Importing the Package

`riemannian_stats` supports both **PascalCase** and **lowercase alias** imports for flexibility:

```python
# Standard
from riemannian_stats import RiemannianAnalysis, DataProcessing, Visualization, Utilities

# Aliased (optional)
from riemannian_stats import riemannian_analysis, data_processing, visualization, utilities
```

💡 *Both styles provide access to the same functionality—choose the one that best fits your coding preferences.*

---

## Installation

Ensure you have [Python ≥ 3.8](https://www.python.org/downloads/) installed, then run:

```bash
pip install riemannian_stats
```

Alternatively, to install from the source code, clone the repository and execute:

```bash
git clone https://github.com/OldemarRodriguez/riemannian_stats.git
cd riemannian_stats
pip install .
```

This project follows PEP 621 and uses pyproject.toml as the primary configuration file.

**Main Dependencies:**

* **matplotlib** (>=3.7.5, <3.11)
* **pandas** (>=2.0.3, <2.3)
* **numpy** (>=1.24.4, <3.0)
* **scikit-learn** (>=1.3.2, <1.7)
* **umap-learn** (>=0.5.7, <0.6)

These dependencies are defined in the [pyproject.toml](pyproject.toml) and in [requirements.txt](requirements.txt) .

---

## License

Distributed under the BSD-3-Clause License. See the [LICENSE.txt](LICENSE.txt) for more details.

---

## 🔍 Testing

The package includes a suite of unit tests located in the `tests/` directory.

To run the tests, make sure [pytest](https://pytest.org/) is installed and that you are in the **root directory** of the project (the one containing both the `riemannian_stats/` package and the `tests/` folder).

Then run:

```bash
pytest
```

This ensures that all functions and modules perform as expected throughout development and maintenance.

---

## Authors & Contributors

- **Oldemar Rodríguez Rojas** – Developed the mathematical functions and conducted the research.
- **Jennifer Lobo Vásquez** – Led the overall development and integration of the package.

## Support & Contributions

If you encounter any issues or have suggestions for improvements, please open an issue on the repository or submit a pull request. Your feedback is invaluable to enhancing the package.

To learn how to contribute effectively, please refer to the [Contributing.md](Contributing.md) file, where you’ll find guidelines and best practices to get involved.

---

## References

- **[Matplotlib Documentation](https://matplotlib.org/stable/contents.html)**  
  Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.  
  PyPI: [matplotlib · PyPI](https://pypi.org/project/matplotlib/)

- **[Pandas Documentation](https://pandas.pydata.org/docs/)**  
  Pandas provides high-performance, easy-to-use data structures and data analysis tools for Python.  
  PyPI: [pandas · PyPI](https://pypi.org/project/pandas/)

- **[NumPy Documentation](https://numpy.org/doc/)**  
  NumPy is the fundamental package for numerical computation in Python.  
  PyPI: [numpy · PyPI](https://pypi.org/project/numpy/)

- **[Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)**  
  Scikit-learn is a machine learning library for Python, providing tools for classification, regression, clustering, and dimensionality reduction.  
  PyPI: [scikit-learn · PyPI](https://pypi.org/project/scikit-learn/)

- **[UMAP-learn Documentation](https://umap-learn.readthedocs.io/)**  
  UMAP (Uniform Manifold Approximation and Projection) is a dimension reduction technique for visualization and general non-linear dimension reduction.  
  PyPI: [umap-learn · PyPI](https://pypi.org/project/umap-learn/)

- **[Setuptools Documentation](https://setuptools.pypa.io/en/latest/)**  
  Setuptools is a package development and distribution tool used to package Python projects and manage dependencies.  
  PyPI: [setuptools · PyPI](https://pypi.org/project/setuptools/)

  
