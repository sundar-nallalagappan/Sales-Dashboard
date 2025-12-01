import pytest
from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_with_negatives():
    transactions = [200.0, 500.0, -50.0, 100.0, 50.0]
    # The expected revenue should only sum the positive values
    expected_revenue = 200.0 + 500.0 + 100.0 + 50.0
    assert calculate_total_revenue(transactions) == expected_revenue

def test_calculate_total_revenue_no_negatives():
    transactions = [100.0, 200.0, 300.0]
    expected_revenue = 600.0
    assert calculate_total_revenue(transactions) == expected_revenue

def test_calculate_total_revenue_only_negatives():
    transactions = [-100.0, -200.0]
    expected_revenue = 0.0
    assert calculate_total_revenue(transactions) == expected_revenue

def test_calculate_total_revenue_empty():
    transactions = []
    expected_revenue = 0.0
    assert calculate_total_revenue(transactions) == expected_revenue
