import pytest
from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_with_negative_values():
    transactions = [200.0, 500.0, -50.0, 100.0, 50.0, -20.0]
    expected_revenue = 200.0 + 500.0 + 100.0 + 50.0  # Only positive values
    assert calculate_total_revenue(transactions) == expected_revenue
