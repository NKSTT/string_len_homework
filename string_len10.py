def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    x1 = s[0]
    x2 = s[-1]
    if x1 == x2:
        return True
    else:
        return False
print (main("ada"))
