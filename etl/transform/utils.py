"""
Utility functions for transformation.
"""


def classify_account(acctbal: float) -> str:
    """
    Classifies account balances into Low, Medium, or High.

    :param acctbal: Account balance.
    :return: Classification string.
    """
    if acctbal < 1000:
        return "Low"
    elif 1000 <= acctbal <= 5000:
        return "Medium"
    else:
        return "High"
