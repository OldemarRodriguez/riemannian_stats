
---

# Riemannian STATS

---

![](/docs/html/_images/logo.jpg)

### 📊 **Riemannian STATS: Statistical Analysis on Riemannian Manifolds**

**RiemannianStats** is an open-source package that implements a novel principal component analysis methodology adapted for data on Riemannian manifolds, using UMAP as a core tool to construct the underlying geometric structure. This tool enables advanced statistical techniques to be applied to any type of dataset, honoring its local geometry, without requiring the data to originate from traditionally geometric domains like medical imaging or shape analysis.

Instead of assuming data resides in Euclidean space, RiemannianStats transforms any data table into a Riemannian manifold by leveraging the local connectivity extracted from a UMAP-generated k-nearest neighbor graph. On top of this structure, the package computes Riemannian principal components, covariance and correlation matrices, and even provides 2D and 3D visualizations that faithfully capture the dataset’s topology.

With **Riemannian STATS**, you can:

* Incorporate the local geometry of your data for meaningful dimensionality reduction.
* Generate visual representations that better reflect the true structure of your data.
* Use a unified framework that generalizes classical statistical analysis to complex geometric contexts.
* Apply these techniques to both synthetic and real high-dimensional datasets.

This package is ideal for researchers, data scientists, and developers seeking to move beyond the traditional assumptions of classical statistics, applying models that respect the intrinsic structure of data.

---

## 🛠️ Features and Usage

**Riemannian STATS** offers several key functionalities:

- **Data Preprocessing:**  
  Easily import and transform datasets using functions in `data_processing.py`.

- **Riemannian Analysis:**  
  Perform advanced statistical methods with `riemannian_analysis.py` for extracting principal components in Riemannian spaces.

- **Visualization:**  
  Generate insightful 2D and 3D plots, along with other visualizations using `visualization.py`.

- **Additional Utilities:**  
  Use helper functions available in `utilities.py` for various tasks.

---

## 📦 Package structure

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
│   ├── __init__.py
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
│
├── requirements.txt                     # Dependencies 
├── pyproject.toml                       # Package installation script
├── README.md                            # General information and usage of the package
└── LICENSE                              # BSD-3-Clause License

```

---

## 🚀 Installation

Ensure you have [Python ≥ 3.6](https://www.python.org/downloads/) installed, then run:

```bash
pip install riemannian_stats
```

Alternatively, to install from the source code, clone the repository and execute:

```bash
git clone https://github.com/JenniLoboV/riemannian_stats.git
cd riemannian_stats
pip install .
```

This project follows PEP 621 and uses pyproject.toml as the primary configuration file.

**Main Dependencies:**

- **matplotlib** (>=3.9.2,<3.11)
- **pandas** (>=2.2.2,<2.3)
- **numpy** (>=1.26.4,<2.0)
- **scikit-learn** (>=1.5.1,<1.7)
- **umap-learn** (>=0.5.7,<0.6)

These dependencies are defined in the [pyproject.toml](./pyproject.toml) and in [requirements.txt](./requirements.txt) .


---

## 🔄 Importing Modules and Classes

RiemannianStats supports multiple import styles to improve flexibility and usability:

### ✅ Standard Imports

Use PascalCase class names for clarity and convention:

```python
from riemannian_stats import RiemannianAnalysis, DataProcessing, Visualization, Utilities
````

### ✨ Lowercase Aliases

Alternatively, you can use lowercase aliases for convenience:

```python
from riemannian_stats import riemannian_analysis, DataProcessing, visualization, utilities
```

Both styles provide access to the same classes—choose the one that fits your workflow best.


---


## 📚 Examples of use
The `examples/` directory contains two comprehensive examples demonstrating how to leverage **Riemannian STATS** for Riemannian data analysis and visualization.

--- 
### Example 1: Iris Dataset

Using the classic Iris dataset (`iris.csv`), this example illustrates the package's capabilities on a well-known, lower-dimensional dataset:

- **Data Loading and Preprocessing:**  
  The Iris dataset is imported using `DataProcessing.load_data()`, with a semicolon as the separator and a dot as the decimal. It checks for a `tipo` column to extract clustering information, which is then separated from the analysis data.

- **Riemannian Analysis:**  
  An instance of `RiemannianAnalysis` is initialized with the dataset and a neighbor count determined as the data length divided by 3. The analysis process includes:
  - Calculation of UMAP graph similarities.
  - Derivation of the rho matrix.
  - Computation of Riemannian vector differences.
  - Generation of the UMAP distance matrix.
  - Calculation of Riemannian covariance and correlation matrices.
  - Extraction of principal components.
  - Determination of explained inertia (as a percentage) using the first two components.
  - Evaluation of correlations between the original variables and principal components.

- **Visualization:**  
  When clustering data is available, the example generates:
  - A **2D scatter plot** with clusters (using dimensions such as `s.largo` and `s.ancho`).
  - A **Principal plane plot** with clusters.
  - A **3D scatter plot** with clusters (adding a third dimension with `p.largo`).
  - A **Correlation circle plot** that is produced in all cases.

*For full details, see [example1.py](./examples/example1.py)*

---

### Example 2: Data10D_250 Dataset

This example demonstrates the analysis of a high-dimensional dataset (`Data10D_250.csv`). The workflow includes:

- **Data Loading and Preprocessing:**  
  The dataset is loaded with `DataProcessing.load_data()`, using a comma as the separator and a dot for decimals. If a `cluster` column exists, clustering information is separated from the main analysis data, while retaining a copy for visualization.

- **Riemannian Analysis:**  
  An instance of `RiemannianAnalysis` is created with a neighbor count calculated as the dataset length divided by 5. The analysis includes:
  - UMAP graph similarities.
  - Computation of the rho matrix.
  - Calculation of Riemannian vector differences.
  - Generation of the UMAP distance matrix.
  - Derivation of Riemannian covariance and correlation matrices.
  - Extraction of principal components from the correlation matrix.
  - Calculation of explained inertia using the first two principal components.

- **Visualization:**  
  Depending on the presence of clustering data, the example produces:
  - A **2D scatter plot** with clusters.
  - A **Principal plane plot** showcasing principal components.
  - A **3D scatter plot** with clusters.
  - A **Correlation circle plot** to display correlations between original variables and principal components.

*For full details, see [example2.py](./examples/example2.py)*

---


## 🔍 Testing

The package includes a suite of unit tests located in the `tests/` directory. To run the tests, ensure [pytest](https://pytest.org/) is installed and run:

```bash
pytest
```

This ensures that all functions and modules perform as expected throughout development and maintenance.

---

## 👥 Authors & Contributors

- **Oldemar Rodríguez Rojas** – Developed the mathematical functions and conducted the research.
- **Jennifer Lobo Vásquez** – Led the overall development and integration of the package.

---

## 📄 License

Distributed under the BSD-3-Clause License. See the [LICENSE](./LICENSE.txt) for more details.

---

## ❓ Support & Contributions

If you encounter any issues or have suggestions for improvements, please open an issue on the repository or submit a pull request. Your feedback is invaluable to enhancing the package.

---
## 📚 References

- **[Matplotlib Documentation](https://matplotlib.org/stable/contents.html)**  
  Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.  
  📦 PyPI: [matplotlib · PyPI](https://pypi.org/project/matplotlib/)

- **[Pandas Documentation](https://pandas.pydata.org/docs/)**  
  Pandas provides high-performance, easy-to-use data structures and data analysis tools for Python.  
  📦 PyPI: [pandas · PyPI](https://pypi.org/project/pandas/)

- **[NumPy Documentation](https://numpy.org/doc/)**  
  NumPy is the fundamental package for numerical computation in Python.  
  📦 PyPI: [numpy · PyPI](https://pypi.org/project/numpy/)

- **[Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)**  
  Scikit-learn is a machine learning library for Python, providing tools for classification, regression, clustering, and dimensionality reduction.  
  📦 PyPI: [scikit-learn · PyPI](https://pypi.org/project/scikit-learn/)

- **[UMAP-learn Documentation](https://umap-learn.readthedocs.io/)**  
  UMAP (Uniform Manifold Approximation and Projection) is a dimension reduction technique for visualization and general non-linear dimension reduction.  
  📦 PyPI: [umap-learn · PyPI](https://pypi.org/project/umap-learn/)

- **[Setuptools Documentation](https://setuptools.pypa.io/en/latest/)**  
  Setuptools is a package development and distribution tool used to package Python projects and manage dependencies.  
  📦 PyPI: [setuptools · PyPI](https://pypi.org/project/setuptools/)

---

```
