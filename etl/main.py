"""
Main ETL script that orchestrates extraction, transformation, and loading.
"""

import os
from etl.extract import (
    extract_customers,
    extract_orders,
    extract_lineitems,
    extract_parts,
    extract_suppliers,
    extract_nations,
    extract_regions,
)
from etl.transform import (
    build_dim_customer,
    build_dim_part,
    build_dim_supplier,
    build_fact_sales,
    build_dim_date,
)
from etl.load import load_to_sql, create_engine_conn


def main() -> None:
    """
    Main function to run the ETL process.
    """
    data_dir = os.path.join(os.getcwd(), "data")

    # Extraction
    df_customers = extract_customers(data_dir)
    df_orders = extract_orders(data_dir)
    df_lineitems = extract_lineitems(data_dir)
    df_parts = extract_parts(data_dir)
    df_suppliers = extract_suppliers(data_dir)
    df_nations = extract_nations(data_dir)
    df_regions = extract_regions(data_dir)

    # Transformation
    dim_customer = build_dim_customer(df_customers)
    dim_part = build_dim_part(df_parts)
    dim_supplier = build_dim_supplier(df_suppliers)
    fact_sales = build_fact_sales(df_orders, df_lineitems)
    dim_date = build_dim_date(fact_sales)

    # Load – using SQLite for demonstration
    engine = create_engine_conn()
    load_to_sql(dim_customer, "DIM_CUSTOMER", engine)
    load_to_sql(dim_part, "DIM_PART", engine)
    load_to_sql(dim_supplier, "DIM_SUPPLIER", engine)
    load_to_sql(fact_sales, "FACT_SALES", engine)
    load_to_sql(dim_date, "DIM_DATE", engine)
    # Optionally load nations & regions for reporting purposes:
    load_to_sql(df_nations, "NATION", engine)
    load_to_sql(df_regions, "REGION", engine)

    print("ETL process complete and data loaded to star_schema.db.")


if __name__ == "__main__":
    main()
