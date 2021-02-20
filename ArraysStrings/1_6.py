import time
import unittest


def compress_string(string):
    N = len(string)
    if N == 0:
        return string

    result = ""
    current_char = string[0]
    count = 0

    for i in range(N):
        if string[i] == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = string[i]
            count = 1

    result += current_char + str(count)
    return min(string, result, key=len)
