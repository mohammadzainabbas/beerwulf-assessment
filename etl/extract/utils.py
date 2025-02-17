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
    return pd.read_csv(
        file_path,
        sep="|",
        header=None,
        names=cols,
        engine="python",
        dtype=col_defs
    )
