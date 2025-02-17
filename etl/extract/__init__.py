"""
Module for data extraction from .tbl files.
"""

from .extract import (
    extract_customers,
    extract_orders,
    extract_lineitems,
    extract_parts,
    extract_suppliers,
    extract_nations,
    extract_regions,
)

__all__ = [
    "extract_customers",
    "extract_orders",
    "extract_lineitems",
    "extract_parts",
    "extract_suppliers",
    "extract_nations",
    "extract_regions",
]
