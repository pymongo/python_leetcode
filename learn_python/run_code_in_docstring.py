def iseven(number):
    """
    Checks if a number is even or odd

    >>> iseven(5)
    False
    >>> assert iseven(6)

    >>> iseven(6)
    True
    """
    return number % 2 == 0


if __name__ == "__main__":
    __import__("doctest").testmod()
