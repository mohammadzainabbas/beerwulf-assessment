import pandas as pd
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine


def load_to_sql(df: pd.DataFrame, table_name: str, engine: Engine) -> None:
    """
    Loads a DataFrame into the SQL table.

    :param df: DataFrame to load.
    :param table_name: Destination table name.
    :param engine: SQLAlchemy engine connection.
    """
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)


def create_engine_conn(db_url: str = "sqlite:///star_schema.db") -> Engine:
    """
    Creates a SQLAlchemy engine connection.

    :param db_url: Database URL.
    :return: SQLAlchemy Engine.
    """
    return create_engine(db_url)
