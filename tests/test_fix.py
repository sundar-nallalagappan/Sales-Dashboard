import unittest
from src.revenue_engine import calculate_total_revenue

class TestRevenueEngine(unittest.TestCase):

    def test_revenue_calculation_with_negatives(self):
        """Test that negative values (refunds) are NOT included in total revenue."""
        transactions = [100.0, 200.0, -50.0, 150.0]
        # Expected revenue should be 100 + 200 + 150 = 450
        self.assertEqual(calculate_total_revenue(transactions), 450.0)

    def test_empty_transactions(self):
        """Test that an empty list of transactions results in zero revenue."""
        self.assertEqual(calculate_total_revenue([]), 0.0)

    def test_all_negative_transactions(self):
        """Test that if all transactions are negative, revenue is zero."""
        transactions = [-100.0, -200.0, -50.0]
        self.assertEqual(calculate_total_revenue(transactions), 0.0)

if __name__ == "__main__":
    unittest.main()
