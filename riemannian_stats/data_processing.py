import pandas as pd


class DataProcessing:
    """
    Utility class for loading and preparing tabular data.

    Provides static methods for reading CSV files into pandas DataFrames, with
    support for custom delimiters and decimal formats. Useful for standardized
    data loading in preprocessing pipelines.
    """

    @staticmethod
    def load_data(filepath: str, separator: str = ";", decimal: str = ".") -> pd.DataFrame:
        """
        Load a CSV file into a pandas DataFrame.

        Parameters:
            filepath (str): Path to the CSV file to be loaded.
            separator (str, optional): Field delimiter used in the CSV file. Default is ";".
            decimal (str, optional): Character to recognize as decimal point. Default is ".".

        Returns:
            pd.DataFrame: DataFrame containing the parsed data from the file.
        """

        return pd.read_csv(filepath, sep=separator, decimal=decimal)
