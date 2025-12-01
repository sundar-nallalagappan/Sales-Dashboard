import pytest
from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_with_negatives():
    # Test case with positive sales and a refund
    transactions = [200.0, 500.0, -50.0, 100.0, 50.0]
    # Expected revenue should only sum positive values as per current logic
    expected_revenue = 200.0 + 500.0 + 100.0 + 50.0  # 850.0
    assert calculate_total_revenue(transactions) == expected_revenue

def test_calculate_total_revenue_all_negatives():
    # Test case with only negative values
    transactions = [-10.0, -20.0, -30.0]
    expected_revenue = 0.0
    assert calculate_total_revenue(transactions) == expected_revenue

def test_calculate_total_revenue_empty():
    # Test case with empty list
    transactions = []
    expected_revenue = 0.0
    assert calculate_total_revenue(transactions) == expected_revenue
