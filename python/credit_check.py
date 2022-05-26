
def credit_check(string):
    """
    This function returns True if the given string is a valid credit card number
    according to the Luhn algorithm.

    Luhn algorithm:
        from the rightmost digit, which is the check digit, moving left, double the value of every other digit
        if product of this doubling operation is greater than 9 (e.g., 7 * 2 = 14)
        then sum the digits of the products (e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5).
        take the sum of all the digits
        if and only if the total modulo 10 is equal to 0 then the number is valid

    Args:
        str (str): The string to check

    Returns:
        bool: True if the given string is a valid credit card number
    """
