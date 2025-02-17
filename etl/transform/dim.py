"""
Build dimension tables.
"""

import pandas as pd
from .utils import classify_account


def build_dim_customer(df_customers: pd.DataFrame) -> pd.DataFrame:
    """
    Builds the Customer Dimension table with a classification.

    :param df_customers: DataFrame containing customer data.
    :return: Transformed customer dimension DataFrame.
    """
    df = df_customers.copy()
    df["C_CLASSIFICATION"] = df["C_ACCTBAL"].apply(classify_account)
    return df


def build_dim_part(df_parts: pd.DataFrame) -> pd.DataFrame:
    """
    Builds the Part Dimension table.

    :param df_parts: DataFrame containing parts data.
    :return: Part dimension DataFrame.
    """
    return df_parts.copy()


def build_dim_supplier(df_suppliers: pd.DataFrame) -> pd.DataFrame:
    """
    Builds the Supplier Dimension table.

    :param df_suppliers: DataFrame containing supplier data.
    :return: Supplier dimension DataFrame.
    """
    return df_suppliers.copy()


def build_dim_date(fact_sales: pd.DataFrame) -> pd.DataFrame:
    """
    Builds a simple Date Dimension table based on order and ship dates.

    :param fact_sales: Fact table DataFrame with date fields.
    :return: Date dimension DataFrame.
    """
    dates = (
        pd.concat([fact_sales["ORDER_DATE"], fact_sales["SHIP_DATE"]])
        .drop_duplicates()
        .reset_index(drop=True)
    )
    df = pd.DataFrame({"DATE": dates})
    df["DAY"] = pd.to_datetime(df["DATE"]).dt.day
    df["MONTH"] = pd.to_datetime(df["DATE"]).dt.month
    df["YEAR"] = pd.to_datetime(df["DATE"]).dt.year
    df["FIN_YEAR"] = pd.to_datetime(df["DATE"]).apply(
        lambda d: d.year if d.month >= 7 else d.year - 1
    )
    return df
