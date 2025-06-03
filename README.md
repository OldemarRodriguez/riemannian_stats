<div align="center">
  <img src="/docs/source/_static/images/logo.jpg" alt="Logo" width="500" height="250"/>
</div>


## 📊 **Riemannian STATS: Statistical Analysis on Riemannian Manifolds**

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

## 🚀 Installation

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

This example illustrates the capabilities of the `riemannian_stats` package using the classic, lower-dimensional **Iris dataset** (`iris.csv`). The analysis follows this workflow:

#### Data Loading and Preprocessing

The dataset is imported using `pandas.read_csv()` with a **semicolon (`;`)** as the separator and a **dot (`.`)** as the decimal mark. Alternatively, you could use `DataProcessing.load_data()` if preferred. The script checks for a `species` column to extract clustering information, separating it from the analysis data but keeping it for visualizations.

#### Riemannian Analysis

An instance of `RiemannianAnalysis` is initialized with a neighbor count equal to the data length divided by 3. The analysis process includes:

* Calculation of **UMAP graph similarities**.
* Derivation of the **rho matrix**.
* Computation of **Riemannian vector differences**.
* Generation of the **UMAP distance matrix**.
* Computation of **Riemannian covariance and correlation matrices**.
* Extraction of **principal components**.
* Determination of **explained inertia** (as a percentage) using the first two components.
* Evaluation of **correlations** between the original variables and principal components.

#### Visualization

When clustering data is available, the example generates:

* A **2D scatter plot** with clusters (using dimensions like `sepal.length` and `sepal.width`).
* A **Principal plane plot** with clusters.
* A **3D scatter plot** with clusters (adding a third dimension with `petal.length`).
* A **Correlation circle plot** (produced in all cases, with or without clusters).

*For full details, see [example1.py](./examples/example1.py)*

---

### Example 2: Data10D_250 Dataset

This example demonstrates the analysis of a high-dimensional dataset (`Data10D_250.csv`). The workflow includes:

#### Data Loading and Preprocessing:
  The dataset is loaded using `pandas.read_csv()` with a comma as the separator and a dot for decimals. Optionally, the user could use `DataProcessing.load_data()` if working within a custom preprocessing pipeline. If a `cluster` column exists, clustering information is separated from the main analysis data, while retaining a copy for visualization.

#### Riemannian Analysis:
  An instance of `RiemannianAnalysis` is created with a neighbor count calculated as the dataset length divided by 5. The analysis includes:

* Calculation of **UMAP graph similarities**.
* Derivation of the **rho matrix**.
* Computation of **Riemannian vector differences**.
* Generation of the **UMAP distance matrix**.
* Computation of **Riemannian covariance and correlation matrices**.
* Extraction of **principal components**.
* Determination of **explained inertia** (as a percentage) using the first two components.
* Evaluation of **correlations** between the original variables and principal components.

#### Visualization:
  Depending on the presence of clustering data, the example produces:

  * A **2D scatter plot** with clusters.
  * A **Principal plane plot** showcasing principal components.
  * A **3D scatter plot** with clusters.
  * A **Correlation circle plot** to display correlations between original variables and principal components.

*For full details, see [example2.py](./examples/example2.py)*

---

---
### Example 3: Olivetti Faces Dataset

This example showcases the use of the `riemannian_stats` package for analyzing a high-dimensional image dataset: the **Olivetti Faces** dataset from `sklearn`.

#### Data Loading and Preprocessing

The dataset is loaded using `fetch_olivetti_faces` and then converted into a `pandas.DataFrame`. Each sample is a flattened grayscale face image, and labels (from 0 to 39) indicate individual identities. These labels are treated as cluster identifiers for visualization.

The number of neighbors for UMAP is calculated based on the number of samples per individual (typically 10), resulting in a value of `n_neighbors = len(data) / 40`.

#### Riemannian Analysis

An instance of `RiemannianAnalysis` is used to compute the following:

* **UMAP similarity matrix**
* **Rho matrix** (`1 - similarity`)
* **Riemannian vector differences**
* **UMAP distance matrix**
* **Riemannian correlation matrix**

From there, the script proceeds to:

* Extract **principal components**
* Calculate the **explained inertia** for the first two components
* Evaluate **correlations** between original features and principal components

#### Visualization

Visualizations are created using the provided cluster labels (individual identities):

* A **2D scatter plot** showing the distribution of individuals in the first two principal components
* A **Principal plane plot** with clusters
* A **3D scatter plot** (adds a third component when available)
* A **Correlation circle plot** showing how original variables relate to the principal components

This example demonstrates how `riemannian_stats` can be extended beyond classical tabular datasets to handle complex **image data**, offering both analytical depth and intuitive visual interpretation.

*For full details, see [example3.py](./examples/example3.py)*

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

## 👥 Authors & Contributors

- **Oldemar Rodríguez Rojas** – Developed the mathematical functions and conducted the research.
- **Jennifer Lobo Vásquez** – Led the overall development and integration of the package.

---

## 📄 License

Distributed under the BSD-3-Clause License. See the [LICENSE](./LICENSE.txt) for more details.

---

## ❓ Support & Contributions

If you encounter any issues or have suggestions for improvements, please open an issue on the repository or submit a pull request. Your feedback is invaluable to enhancing the package.

To learn how to contribute effectively, please refer to the [Contributing.md](./Contributing.md) file, where you’ll find guidelines and best practices to get involved.

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

