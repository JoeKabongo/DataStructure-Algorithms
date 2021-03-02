# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures
def is_unique(string):
    already_seen = set()
    for char in string:
        if char in already_seen:
            return False
        already_seen.add(char)
    return True


def is_unique_nospace(string):
    N = len(string)
    for i in range(N):
        char = string[i]
        for j in range(i+1, N):
            if char == string[j]:
                return False
    
    return True