Module Details
===============

The ``DataProcessing`` module simplifies the task of loading tabular data from CSV files into pandas DataFrames. It is particularly useful for quickly preparing datasets with different delimiters and decimal formats for analysis workflows.

Overview
--------

This utility module provides a static method to read CSV files, allowing you to define both the field separator and decimal character. It ensures seamless integration with datasets that use various locale-specific formats, reducing friction in the data preparation phase.

Key Capabilities
----------------

- **Flexible CSV Importing**: Easily load CSVs with custom separators and decimal characters.
- **Pandas DataFrame Output**: Automatically returns a clean DataFrame ready for analysis.
- **No Instantiation Required**: The static design allows you to call methods directly, simplifying code in notebooks and scripts.

Use Cases
---------

This module is especially useful when:

- You’re working with CSV files that use non-standard formats (e.g., semicolons or commas as decimal separators).
- You want a consistent, reusable method for importing datasets in your preprocessing pipeline.
- You need a fast and reliable way to load data into pandas across multiple scripts or notebooks.

Usage Example
-------------

Here is a basic example showing how to load a dataset using ``DataProcessing``:

.. code-block:: python

   from riemannian_stats.data_processing import DataProcessing

   # Load a CSV file using a custom separator and decimal format
   df = DataProcessing.load_data("path/to/data.csv", separator=",", decimal=".")

   # DataFrame is now ready for analysis
   print(df.head())

For detailed examples of how this module integrates into a full data analysis workflow, refer to the **"How to Use Riemannian STATS"** section, available from both the documentation homepage and the sidebar.

API Documentation
--------------------

.. autoclass:: riemannian_stats.data_processing.DataProcessing
   :members:
   :undoc-members:
   :show-inheritance:
