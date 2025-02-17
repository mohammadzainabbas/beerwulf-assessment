"""
Extract data from `.tbl` files.
"""

import os
import pandas as pd
from .utils import read_tbl


def extract_customers(data_dir: str) -> pd.DataFrame:
    """
    Extracts customer data using column definitions.
    
    :param data_dir: Directory containing data files.
    :return: DataFrame with customer records.
    """
    col_defs = {
        "C_CUSTKEY": int,
        "C_NAME": str,
        "C_ADDRESS": str,
        "C_NATIONKEY": int,
        "C_PHONE": str,
        "C_ACCTBAL": float,
        "C_MKTSEGMENT": str,
        "C_COMMENT": str
    }
    return read_tbl(os.path.join(data_dir, "customer.tbl"), col_defs)

def extract_orders(data_dir: str) -> pd.DataFrame:
    """
    Extracts orders data using column definitions.
    
    :param data_dir: Directory containing data files.
    :return: DataFrame with order records.
    """
    col_defs = {
        "O_ORDERKEY": int,
        "O_CUSTKEY": int,
        "O_ORDERSTATUS": str,
        "O_TOTALPRICE": float,
        "O_ORDERDATE": str,  # Convert to datetime later if needed.
        "O_ORDERPRIORITY": str,
        "O_CLERK": str,
        "O_SHIPPRIORITY": int,
        "O_COMMENT": str
    }
    return read_tbl(os.path.join(data_dir, "orders.tbl"), col_defs)

def extract_lineitems(data_dir: str) -> pd.DataFrame:
    """
    Extracts line item data using column definitions.
    
    :param data_dir: Directory containing data files.
    :return: DataFrame with line item records.
    """
    col_defs = {
        "L_ORDERKEY": int,
        "L_PARTKEY": int,
        "L_SUPPKEY": int,
        "L_LINENUMBER": int,
        "L_QUANTITY": int,
        "L_EXTENDEDPRICE": float,
        "L_DISCOUNT": float,
        "L_TAX": float,
        "L_RETURNFLAG": str,
        "L_LINESTATUS": str,
        "L_SHIPDATE": str,
        "L_COMMITDATE": str,
        "L_RECEIPTDATE": str,
        "L_SHIPINSTRUCT": str,
        "L_SHIPMODE": str,
        "L_COMMENT": str
    }
    return read_tbl(os.path.join(data_dir, "lineitem.tbl"), col_defs)

def extract_parts(data_dir: str) -> pd.DataFrame:
    """
    Extracts parts data using column definitions.
    
    :param data_dir: Directory containing data files.
    :return: DataFrame with parts records.
    """
    col_defs = {
        "P_PARTKEY": int,
        "P_NAME": str,
        "P_MFGR": str,
        "P_BRAND": str,
        "P_TYPE": str,
        "P_SIZE": int,
        "P_CONTAINER": str,
        "P_RETAILPRICE": float,
        "P_COMMENT": str
    }
    return read_tbl(os.path.join(data_dir, "part.tbl"), col_defs)

def extract_suppliers(data_dir: str) -> pd.DataFrame:
    """
    Extracts supplier data using column definitions.
    
    :param data_dir: Directory containing data files.
    :return: DataFrame with supplier records.
    """
    col_defs = {
        "S_SUPPKEY": int,
        "S_NAME": str,
        "S_ADDRESS": str,
        "S_NATIONKEY": int,
        "S_PHONE": str,
        "S_ACCTBAL": float,
        "S_COMMENT": str
    }
    return read_tbl(os.path.join(data_dir, "supplier.tbl"), col_defs)

def extract_nations(data_dir: str) -> pd.DataFrame:
    """
    Extracts nation data using column definitions.
    
    :param data_dir: Directory containing data files.
    :return: DataFrame with nation records.
    """
    col_defs = {
        "N_NATIONKEY": int,
        "N_NAME": str,
        "N_REGIONKEY": int,
        "N_COMMENT": str
    }
    return read_tbl(os.path.join(data_dir, "nation.tbl"), col_defs)

def extract_regions(data_dir: str) -> pd.DataFrame:
    """
    Extracts region data using column definitions.
    
    :param data_dir: Directory containing data files.
    :return: DataFrame with region records.
    """
    col_defs = {
        "R_REGIONKEY": int,
        "R_NAME": str,
        "R_COMMENT": str
    }
    return read_tbl(os.path.join(data_dir, "region.tbl"), col_defs)