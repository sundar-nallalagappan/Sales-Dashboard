
import unittest
from src.revenue_engine import calculate_total_revenue

class TestRevenueCalculation(unittest.TestCase):

    def test_ignores_negative_transactions(self):
        """Test that negative transaction amounts (refunds) are ignored."""
        transactions = [100.0, 200.0, -50.0, 300.0, -20.0]
        expected_revenue = 100.0 + 200.0 + 300.0  # Only positive values should sum up
        actual_revenue = calculate_total_revenue(transactions)
        self.assertEqual(actual_revenue, expected_revenue)

if __name__ == "__main__":
    unittest.main()
