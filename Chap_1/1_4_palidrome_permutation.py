def palidrome_permutation(string):
    freq = {}
    odds = 0

    for char in string:
        freq[char] = freq.get(char, 0) + 1
        if freq[char] % 2 == 0:
            odds -= 1
        else:
            odds += 1

    return odds <= 1
