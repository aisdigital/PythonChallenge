import pandas as pd


def read_and_store_CSV(CSV_file_loc):
    """Read a CSV file and store the data in memory

    Args:
        CSV_file_loc (str): The CSV file location

    Returns:
        data (DataFrame): two-dimensional data structure with labeled axes with CSV data
    """

    return pd.read_csv(CSV_file_loc, dtype={"SALECODE": str})
