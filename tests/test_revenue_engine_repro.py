import unittest
from src.revenue_engine import calculate_total_revenue

class TestRevenueEngine(unittest.TestCase):

    def test_calculate_total_revenue_with_negatives(self):
        """Test that negative values (refunds) are ignored."""
        transactions = [100.0, 200.0, -50.0, 300.0, -100.0]
        expected_revenue = 600.0  # 100 + 200 + 300
        self.assertEqual(calculate_total_revenue(transactions), expected_revenue)

    def test_calculate_total_revenue_all_positives(self):
        """Test with only positive values."""
        transactions = [150.0, 250.0, 350.0]
        expected_revenue = 750.0
        self.assertEqual(calculate_total_revenue(transactions), expected_revenue)

    def test_calculate_total_revenue_empty(self):
        """Test with an empty list of transactions."""
        transactions = []
        expected_revenue = 0.0
        self.assertEqual(calculate_total_revenue(transactions), expected_revenue)

    def test_calculate_total_revenue_all_negatives(self):
        """Test with only negative values."""
        transactions = [-50.0, -100.0, -20.0]
        expected_revenue = 0.0
        self.assertEqual(calculate_total_revenue(transactions), expected_revenue)
