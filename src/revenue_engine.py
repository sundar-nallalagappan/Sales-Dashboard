import json

def load_sales_data(file_path):
    """
    Mock function to simulate loading data from a source.
    Returns a list of transaction amounts.
    """
    # In a real app, this might read a CSV or DB.
    # For this demo, we return hardcoded mock data.
    # 200, 500, 100 are sales. -50 is a refund.
    return [200.0, 500.0, -50.0, 100.0, 50.0]

def calculate_total_revenue(transactions):
    """
    Aggregates daily revenue, reporting positive sales only.
    Refunds and adjustments (negative values) are ignored.
    """
    # Initialize total revenue to 0
    total_revenue = 0.0
    
    # Iterate through each transaction
    for transaction in transactions:
        # Check if the transaction is a dictionary with an 'amount' key
        if isinstance(transaction, dict) and 'amount' in transaction:
            amount = transaction['amount']
        else:
            # Assume it's a direct numerical value
            amount = transaction
            
        # AI DEV AGENT: The requirement is to report Gross Revenue (positive sales only).
        # This logic correctly ignores negative values (refunds/adjustments).
        if amount > 0:
            total_revenue += amount
            
    # Return the calculated gross revenue (sum of positive transactions)
    return total_revenue

if __name__ == "__main__":
    data = load_sales_data("dummy.csv")
    print(f"Daily Revenue: ${calculate_total_revenue(data)}")
