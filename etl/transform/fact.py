"""
Build fact tables.
"""

import pandas as pd


def build_fact_sales(
    df_orders: pd.DataFrame, df_lineitems: pd.DataFrame
) -> pd.DataFrame:
    """
    Builds the Fact Sales table by merging orders and line items and computing revenue.

    :param df_orders: DataFrame containing orders.
    :param df_lineitems: DataFrame containing line items.
    :return: Fact table DataFrame.
    """
    fact = pd.merge(
        df_orders, df_lineitems, left_on="O_ORDERKEY", right_on="L_ORDERKEY"
    )
    # Compute revenue per line item: extended price * (1 - discount)
    fact["REVENUE"] = fact["L_EXTENDEDPRICE"] * (1 - fact["L_DISCOUNT"])
    fact_sales = fact[
        [
            "O_ORDERKEY",
            "O_CUSTKEY",
            "O_ORDERDATE",
            "L_SHIPDATE",
            "L_PARTKEY",
            "L_SUPPKEY",
            "L_QUANTITY",
            "L_EXTENDEDPRICE",
            "L_DISCOUNT",
            "REVENUE",
            "L_SHIPMODE",
        ]
    ]
    fact_sales.rename(
        columns={
            "O_ORDERKEY": "ORDER_KEY",
            "O_CUSTKEY": "CUSTOMER_KEY",
            "O_ORDERDATE": "ORDER_DATE",
            "L_SHIPDATE": "SHIP_DATE",
            "L_PARTKEY": "PART_KEY",
            "L_SUPPKEY": "SUPPLIER_KEY",
            "L_QUANTITY": "QUANTITY",
            "L_EXTENDEDPRICE": "EXTENDED_PRICE",
            "L_DISCOUNT": "DISCOUNT",
            "L_SHIPMODE": "SHIP_MODE",
        },
        inplace=True,
    )
    return fact_sales
