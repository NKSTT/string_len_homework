def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    
    if len(s1)%2 != 0 and len(s2)%2 != 0 and len(s3)%2 == 0:
        return s1, s2
    elif len(s1)%2 != 0 and len(s2)%2 == 0 and len(s3)%2 != 0:
        return s1, s3
    elif len(s1)%2 == 0 and len(s2)%2 != 0 and len(s3)%2 != 0:
        return s2, s3

    if len(s1)%2 == 0 and len(s2)%2 == 0 and len(s3)%2 != 0:
        return s3
    elif len(s1)%2 == 0 and len(s2)%2 != 0 and len(s3)%2 == 0:
        return s2
    elif len(s1)%2 != 0 and len(s2)%2 == 0 and len(s3)%2 == 0:
        return s1
    else:
        return s1, s2, s3
    
print (main('qwer','hkkk','qwertyui'))