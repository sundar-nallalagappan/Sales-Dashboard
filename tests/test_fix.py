import pytest
from src.revenue_engine import calculate_total_revenue

def test_calculate_total_revenue_with_negative_values():
    """
    Test that calculate_total_revenue correctly handles negative values (refunds).
    The current implementation should fail this test if negative values are included.
    """
    transactions = [200.0, 500.0, -50.0, 100.0, 50.0, -20.0]
    # Expected gross revenue should only sum positive values: 200 + 500 + 100 + 50 = 850
    expected_gross_revenue = 850.0
    
    actual_revenue = calculate_total_revenue(transactions)
    
    # This assertion will fail with the current implementation because it sums all values
    # including negative ones.
    assert actual_revenue == expected_gross_revenue

def test_calculate_total_revenue_with_only_negative_values():
    """
    Test that calculate_total_revenue returns 0 when only negative values are present.
    """
    transactions = [-50.0, -20.0]
    expected_gross_revenue = 0.0
    actual_revenue = calculate_total_revenue(transactions)
    assert actual_revenue == expected_gross_revenue

def test_calculate_total_revenue_with_mixed_data_types():
    """
    Test that calculate_total_revenue handles mixed data types, including dictionaries.
    """
    transactions = [200.0, {'amount': 500.0}, -50.0, {'amount': 100.0}, 50.0]
    expected_gross_revenue = 850.0
    actual_revenue = calculate_total_revenue(transactions)
    assert actual_revenue == expected_gross_revenue

def test_calculate_total_revenue_empty_list():
    """
    Test that calculate_total_revenue returns 0 for an empty list.
    """
    transactions = []
    expected_gross_revenue = 0.0
    actual_revenue = calculate_total_revenue(transactions)
    assert actual_revenue == expected_gross_revenue

def test_calculate_total_revenue_with_zero_values():
    """
    Test that calculate_total_revenue handles zero values correctly.
    """
    transactions = [200.0, 0.0, 500.0, -50.0]
    expected_gross_revenue = 700.0
    actual_revenue = calculate_total_revenue(transactions)
    assert actual_revenue == expected_gross_revenue


