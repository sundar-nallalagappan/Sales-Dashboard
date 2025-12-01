import pytest
from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_with_negatives():
    transactions = [200.0, 500.0, -50.0, 100.0, 50.0]
    # Expected gross revenue should ignore the -50.0 refund
    expected_revenue = 200.0 + 500.0 + 100.0 + 50.0
    assert calculate_total_revenue(transactions) == expected_revenue
