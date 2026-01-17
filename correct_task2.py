# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import re


def count_valid_emails(emails):
    """
    Count the number of valid email addresses in the provided list.

    Parameters:
    emails (list): A list of email addresses as strings.

    Returns:
    int: The count of valid email addresses. A valid email must contain an "@" symbol and follow standard email formatting.

    Raises:
    ValueError: If the input is not a list.
    """

    # Ensure the input is a list
    if not isinstance(emails, list):
        raise ValueError("Input must be a list of emails.")

    count = 0
    # Regular expression for validating an email
    email_pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )

    for email in emails:
        # Check if the email is a string and matches the regex pattern
        if isinstance(email, str) and email_pattern.match(email):
            count += 1

    return count
