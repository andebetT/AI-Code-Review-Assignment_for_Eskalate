# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    """
    Calculate the average of valid measurements, ignoring None values.

    Parameters:
    values (list): A list of measurements, which may include None or invalid types.

    Returns:
    float: The average of the valid measurements, or 0.0 if no valid measurements are found.

    Raises:
    ValueError: If the input is not a list.
    """

    # Ensure the input is a list
    if not isinstance(values, list):
        raise ValueError("Input must be a list of values.")

    total = 0
    valid_count = 0

    for v in values:
        if v is not None and isinstance(v, (int, float)):  # Check for valid numeric types
            total += float(v)
            valid_count += 1

    # Return 0.0 if no valid measurements are found to avoid division by zero
    return total / valid_count if valid_count > 0 else 0.0
