import unittest
from src.revenue_engine import calculate_total_revenue

class TestRevenueFix(unittest.TestCase):

    def test_negative_transactions_are_excluded(self):
        """Test that negative transactions (refunds) do not affect the gross revenue."""
        # Mock transactions including sales and refunds
        transactions = [200.0, 500.0, -50.0, 100.0, 50.0, -20.0]
        
        # Expected gross revenue: sum of positive values only
        # 200 + 500 + 100 + 50 = 850
        expected_revenue = 850.0
        
        # Calculate actual revenue using the function
        actual_revenue = calculate_total_revenue(transactions)
        
        # Assert that the actual revenue matches the expected revenue
        self.assertEqual(actual_revenue, expected_revenue, "The calculate_total_revenue function did not correctly exclude negative values.")

    def test_only_positive_transactions_are_summed(self):
        """Test that only positive transactions contribute to the total gross revenue."""
        transactions = [100.0, -20.0, 300.0, -50.0, 50.0]
        # Expected: 100 + 300 + 50 = 450
        expected_revenue = 450.0
        actual_revenue = calculate_total_revenue(transactions)
        self.assertEqual(actual_revenue, expected_revenue, "The calculate_total_revenue function should only sum positive transaction amounts.")

if __name__ == '__main__':
    unittest.main()
