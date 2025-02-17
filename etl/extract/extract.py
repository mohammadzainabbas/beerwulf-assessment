"""
Extract data from `.tbl` files.
"""

import os
import pandas as pd
from .utils import read_tbl


def extract_customers(data_dir: str) -> pd.DataFrame:
    """
    Extracts customer data.

    :param data_dir: Directory containing data files.
    :return: DataFrame with customer records.
    """
    cols = [
        "C_CUSTKEY",
        "C_NAME",
        "C_ADDRESS",
        "C_NATIONKEY",
        "C_PHONE",
        "C_ACCTBAL",
        "C_MKTSEGMENT",
        "C_COMMENT",
    ]
    return read_tbl(os.path.join(data_dir, "customer.tbl"), cols)


def extract_orders(data_dir: str) -> pd.DataFrame:
    """
    Extracts orders data.

    :param data_dir: Directory containing data files.
    :return: DataFrame with order records.
    """
    cols = [
        "O_ORDERKEY",
        "O_CUSTKEY",
        "O_ORDERSTATUS",
        "O_TOTALPRICE",
        "O_ORDERDATE",
        "O_ORDERPRIORITY",
        "O_CLERK",
        "O_SHIPPRIORITY",
        "O_COMMENT",
    ]
    return read_tbl(os.path.join(data_dir, "orders.tbl"), cols)


def extract_lineitems(data_dir: str) -> pd.DataFrame:
    """
    Extracts line item data.

    :param data_dir: Directory containing data files.
    :return: DataFrame with line item records.
    """
    cols = [
        "L_ORDERKEY",
        "L_PARTKEY",
        "L_SUPPKEY",
        "L_LINENUMBER",
        "L_QUANTITY",
        "L_EXTENDEDPRICE",
        "L_DISCOUNT",
        "L_TAX",
        "L_RETURNFLAG",
        "L_LINESTATUS",
        "L_SHIPDATE",
        "L_COMMITDATE",
        "L_RECEIPTDATE",
        "L_SHIPINSTRUCT",
        "L_SHIPMODE",
        "L_COMMENT",
    ]
    return read_tbl(os.path.join(data_dir, "lineitem.tbl"), cols)


def extract_parts(data_dir: str) -> pd.DataFrame:
    """
    Extracts parts data.

    :param data_dir: Directory containing data files.
    :return: DataFrame with parts records.
    """
    cols = [
        "P_PARTKEY",
        "P_NAME",
        "P_MFGR",
        "P_BRAND",
        "P_TYPE",
        "P_SIZE",
        "P_CONTAINER",
        "P_RETAILPRICE",
        "P_COMMENT",
    ]
    return read_tbl(os.path.join(data_dir, "part.tbl"), cols)


def extract_suppliers(data_dir: str) -> pd.DataFrame:
    """
    Extracts suppliers data.

    :param data_dir: Directory containing data files.
    :return: DataFrame with supplier records.
    """
    cols = [
        "S_SUPPKEY",
        "S_NAME",
        "S_ADDRESS",
        "S_NATIONKEY",
        "S_PHONE",
        "S_ACCTBAL",
        "S_COMMENT",
    ]
    return read_tbl(os.path.join(data_dir, "supplier.tbl"), cols)


def extract_nations(data_dir: str) -> pd.DataFrame:
    """
    Extracts nation data.

    :param data_dir: Directory containing data files.
    :return: DataFrame with nation records.
    """
    cols = ["N_NATIONKEY", "N_NAME", "N_REGIONKEY", "N_COMMENT"]
    return read_tbl(os.path.join(data_dir, "nation.tbl"), cols)


def extract_regions(data_dir: str) -> pd.DataFrame:
    """
    Extracts region data.

    :param data_dir: Directory containing data files.
    :return: DataFrame with region records.
    """
    cols = ["R_REGIONKEY", "R_NAME", "R_COMMENT"]
    return read_tbl(os.path.join(data_dir, "region.tbl"), cols)
