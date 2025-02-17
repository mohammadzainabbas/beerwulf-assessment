"""
Utility functions for extraction.
"""

from typing import Dict, Any
import pandas as pd


def read_tbl(file_path: str, col_defs: Dict[str, Any]) -> pd.DataFrame:
    """
    Reads a .tbl file into a pandas DataFrame using column definitions that include both names and dtypes.

    :param file_path: Path to the .tbl file.
    :param col_defs: Dictionary mapping column names to their expected data types.
    :return: DataFrame with the data and proper dtypes.
    """
    cols = list(col_defs.keys())
    # Read all columns as string to avoid early conversion issues.
    df = pd.read_csv(file_path, sep="|", header=None, engine="python", dtype=str)
    # If there are extra columns (due to trailing delimiters), keep only the expected number.
    if df.shape[1] > len(cols):
        df = df.iloc[:, : len(cols)]
    df.columns = cols
    # Cast each column to its defined type.
    for col, dtype in col_defs.items():
        df[col] = df[col].astype(dtype)
    return df
