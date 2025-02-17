"""
Utility functions for extraction.
"""

from typing import List
import pandas as pd

def read_tbl(file_path: str, names: List[str]) -> pd.DataFrame:
    """
    Reads a .tbl file into a pandas DataFrame.
    
    :param file_path: Path to the .tbl file.
    :param names: List of column names.
    :return: DataFrame with the data.
    """
    # The extra column is dropped due to trailing delimiter issues.
    return pd.read_csv(file_path, sep="|", header=None, names=names, engine="python").drop(columns=[len(names)])
