
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

    digits = [int(digit) for digit in string]

    # for i, el in enumerate(list(reversed(digits))):
    #     pass

    # for i in range(len(digits) - 2, -1, -2):
    #     digits[i]

    new_digits = list()

    for i, digit in enumerate(digits[::-1]):  # we're going backwards through the list
        if i % 2 == 1:
            new_digit = digit * 2

            if new_digit < 10:
                new_digits.append(new_digit)
            else:
                new_digits.append(sum(int(digit) for digit in str(new_digit)))
        else:
            new_digits.append(digit)

    return "The number is valid!" if sum(new_digits) % 10 == 0 else "The number is invalid!"


result = credit_check('5541808923795240')  # "The number is valid!"
print(result)
result = credit_check("4024007136512380")  # "The number is valid!"
print(result)
result = credit_check("6011797668867828")  # "The number is valid!"
print(result)
