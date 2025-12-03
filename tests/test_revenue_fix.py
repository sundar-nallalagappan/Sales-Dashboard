import pytest
from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_with_negatives():
    """
    Test that negative transactions (refunds) are ignored in revenue calculation.
    """
    transactions = [100.0, 200.0, -50.0, 300.0, -20.0]
    # Expected revenue should only sum positive values: 100 + 200 + 300 = 600
    expected_revenue = 600.0
    assert calculate_total_revenue(transactions) == expected_revenue
