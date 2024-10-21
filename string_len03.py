def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    a = "code"
    b = "exam"
    if len(a)==len(b):
        return True
    else:
        return False
x = main(1,1)
print(x)