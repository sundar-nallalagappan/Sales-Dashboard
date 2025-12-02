import pytest
from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_ignores_negatives():
    """
    Test that negative transaction values (refunds) are ignored.
    The expected revenue should only sum positive values.
    """
    transactions = [100.0, 200.0, -50.0, 300.0, -100.0]
    # Expected: 100.0 + 200.0 + 300.0 = 600.0
    assert calculate_total_revenue(transactions) == 600.0

def test_calculate_total_revenue_empty():
    """
    Test that an empty list of transactions results in 0 revenue.
    """
    transactions = []
    assert calculate_total_revenue(transactions) == 0.0

def test_calculate_total_revenue_all_negatives():
    """
    Test that if all transactions are negative, the revenue is 0.
    """
    transactions = [-100.0, -200.0, -50.0]
    assert calculate_total_revenue(transactions) == 0.0

def test_calculate_total_revenue_mixed_values():
    """
    Test with a mix of positive and negative values, including zero.
    """
    transactions = [150.0, -75.0, 0.0, 225.0, -30.0]
    # Expected: 150.0 + 0.0 + 225.0 = 375.0
    assert calculate_total_revenue(transactions) == 375.0
