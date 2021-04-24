def string_rotation(s1, s2):
    N = len(s1)
    if N == len(s2) and N != 0:
        return s2 in s1+s1

    return False
