def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}
    for c in s1:
        freq[c] = freq.get(c, 0) + 1

    for char in s2:
        if freq.get(char, 0) == 0:
            return False
        freq[char] -= 1

    return True
