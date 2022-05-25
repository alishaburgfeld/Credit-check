

def digit_sum(n):
    """
    This function returns the sum of the digits of the given number.

    Args:
        n (int): The number

    Returns:
        int: The sum of the digits of the given number
    """

    return sum(int(digit) for digit in str(n))


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

    nums = [int(digit) for digit in string]

    for i in range(len(nums) - 2, -1, -2):
        nums[i] *= 2
        if nums[i] > 9:
            nums[i] = digit_sum(nums[i])

    return "The number is valid!" if sum(nums) % 10 == 0 else "The number is invalid!"
