# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    """
    Calculate the average order value for non-cancelled orders.

    Parameters:
    orders (list): A list of dictionaries, where each dictionary represents an order.
                   Each order must contain 'status' and 'amount' keys.

    Returns:
    float: The average order value. Returns 0.0 if there are no valid orders.

    Raises:
    ValueError: If the input is not a list or if any order is missing required keys.
    """

    # Early return if the orders list is empty or None
    if not orders:
        return 0.0

    if not isinstance(orders, list):
        raise ValueError("Input must be a list of orders.")

    total = 0
    valid_order_count = 0

    for order in orders:
        if not isinstance(order, dict):
            raise ValueError("Each order must be a dictionary.")
        if 'status' not in order or 'amount' not in order:
            raise ValueError("Each order must have 'status' and 'amount' keys.")

        if order["status"] != "cancelled":
            total += order["amount"]
            valid_order_count += 1

    # Return 0.0 if there are no valid orders
    return total / valid_order_count if valid_order_count > 0 else 0.0


