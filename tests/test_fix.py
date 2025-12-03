import pytest
from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_with_negatives():
    """
    Test that negative values (refunds) are ignored in total revenue calculation.
    """
    transactions = [200.0, 500.0, -50.0, 100.0, 50.0]
    # Expected revenue should only sum positive values: 200 + 500 + 100 + 50 = 850
    expected_revenue = 850.0
    assert calculate_total_revenue(transactions) == expected_revenue
