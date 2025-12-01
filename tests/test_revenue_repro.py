import pytest
from src.revenue_engine import calculate_total_revenue

def test_negative_values_under_reporting():
    sales_data = [
        100,
        200,
        -50, # Refund/Adjustment
        150
    ]
    # Expected: 100 + 200 + 150 = 450 (Negative value should be ignored)
    assert calculate_total_revenue(sales_data) == 450
