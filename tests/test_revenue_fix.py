import pytest

from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_with_negative_values():
    """
    Test that negative values (refunds) are ignored in total revenue calculation.
    """
    transactions = [200.0, 500.0, -50.0, 100.0, 50.0]
    # Expected revenue should only sum positive values: 200 + 500 + 100 + 50 = 850.0
    expected_revenue = 850.0
    actual_revenue = calculate_total_revenue(transactions)
    assert actual_revenue == expected_revenue

def test_calculate_total_revenue_all_positive():
    """
    Test with only positive values.
    """
    transactions = [100.0, 200.0, 300.0]
    expected_revenue = 600.0
    actual_revenue = calculate_total_revenue(transactions)
    assert actual_revenue == expected_revenue

def test_calculate_total_revenue_all_negative():
    """
    Test with only negative values.
    """
    transactions = [-100.0, -200.0, -50.0]
    expected_revenue = 0.0
    actual_revenue = calculate_total_revenue(transactions)
    assert actual_revenue == expected_revenue

def test_calculate_total_revenue_empty():
    """
    Test with an empty list of transactions.
    """
    transactions = []
    expected_revenue = 0.0
    actual_revenue = calculate_total_revenue(transactions)
    assert actual_revenue == expected_revenue
