How to Install It
==================

To install the **Riemannian STATS** package, you can use **pip** from the Python Package Index (PyPI), directly from GitHub, or by building and installing it locally from source.

We strongly recommend installing the package inside a **virtual environment** to avoid conflicts with other Python packages.

.. note::

   You can create and activate a virtual environment with:

   .. code-block:: bash

      python -m venv .venv
      source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

Install via PyPI
----------------

To install the latest version of **Riemannian STATS** directly from PyPI, simply run:

.. code-block:: bash

   pip install riemannian_stats

This will automatically install the package along with its required dependencies.

Install from GitHub
-------------------

To install the latest development version directly from the GitHub repository:

.. code-block:: bash

   pip install git+https://github.com/OldemarRodriguez/riemannian_stats.git

This method does not require cloning the repository manually.

Install from Local Source
-------------------------

If you prefer to clone the repository and install the package from local files:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/OldemarRodriguez/riemannian_stats.git

2. Navigate to the project directory:

   .. code-block:: bash

      cd riemannian_stats

3. Install the package:

   .. code-block:: bash

      pip install .

Install from a Local tar.gz File
--------------------------------

If you have the package file ``riemannian_stats-0.1.0.tar.gz`` on your computer, follow these steps to install it locally:

1. Open the **Command Prompt** (CMD) or **Terminal**.
2. Use the ``cd`` command to go to the folder where the file is located.
3. Run the following command:

   .. code-block:: bash

      pip install riemannian_stats-0.1.0.tar.gz

That's it! The package will be installed into your current Python environment.


Requirements
-------------

Make sure you have the necessary dependencies listed in the `requirements.txt` file. The core dependencies include:

- **matplotlib** (>=3.9.2,<3.11)
- **pandas** (>=2.2.2,<2.3)
- **numpy** (>=1.26.4,<2.0)
- **scikit-learn** (>=1.5.1,<1.7)
- **umap-learn** (>=0.5.7,<0.6)

These dependencies are automatically installed with `pip install`, but you can also install them manually:

.. code-block:: bash

   pip install -r requirements.txt

Python Version
---------------

**Riemannian STATS** requires Python version **3.8 or higher**. You can check your current Python version with:

.. code-block:: bash

   python --version

For more detailed installation instructions or to contribute to the project, visit the `GitHub repository <https://github.com/OldemarRodriguez/riemannian_stats.git>`_.
