import unittest
from src.revenue_engine import calculate_total_revenue

class TestRevenueCalculation(unittest.TestCase):

    def test_negative_values_ignored(self):
        """Test that negative transaction values (refunds) are ignored."""
        transactions = [200.0, 500.0, -50.0, 100.0, 50.0]
        expected_revenue = 850.0  # 200 + 500 + 100 + 50
        self.assertEqual(calculate_total_revenue(transactions), expected_revenue)

    def test_all_positive_values(self):
        """Test with only positive transaction values."""
        transactions = [100.0, 200.0, 300.0]
        expected_revenue = 600.0
        self.assertEqual(calculate_total_revenue(transactions), expected_revenue)

    def test_all_negative_values(self):
        """Test with only negative transaction values."""
        transactions = [-100.0, -200.0, -50.0]
        expected_revenue = 0.0
        self.assertEqual(calculate_total_revenue(transactions), expected_revenue)

    def test_empty_transactions(self):
        """Test with an empty list of transactions."""
        transactions = []
        expected_revenue = 0.0
        self.assertEqual(calculate_total_revenue(transactions), expected_revenue)

if __name__ == '__main__':
    unittest.main()
