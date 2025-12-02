import pytest
from src.revenue_engine import calculate_total_revenue

def test_revenue_calculation_with_negatives():
    """Tests that negative values (refunds) are ignored in revenue calculation."""
    transactions = [200.0, 500.0, -50.0, 100.0, -20.0, 50.0]
    # Expected revenue: 200 + 500 + 100 + 50 = 850.0
    assert calculate_total_revenue(transactions) == 850.0

def test_revenue_calculation_with_only_negatives():
    """Tests that if only negative values are present, revenue is 0."""
    transactions = [-50.0, -20.0, -100.0]
    assert calculate_total_revenue(transactions) == 0.0

def test_revenue_calculation_with_no_negatives():
    """Tests standard positive sales calculation."""
    transactions = [100.0, 200.0, 300.0]
    assert calculate_total_revenue(transactions) == 600.0

def test_revenue_calculation_with_empty_list():
    """Tests calculation with an empty transaction list."""
    transactions = []
    assert calculate_total_revenue(transactions) == 0.0
