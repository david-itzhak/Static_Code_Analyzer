def get_number(num):
    """Return the number one less than the given positive number.
    If the number is nonpositive, return a string "Enter a positive number!".

    Arguments:
    num -- an integer.
    Return values:
    An integer one less than the input number.
    """
    return num - 1 if num > 0 else "Enter a positive number!"
