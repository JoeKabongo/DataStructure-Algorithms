def urlify(s, size):
    """ replace all space with %20"""
    N = len(s)
    array = list(s)
    new_index = N - 1

    for i in range(size-1, -1, -1):
        if s[i] == ' ':
            # replace spaces
            array[new_index] = '0'
            array[new_index-1] = '2'
            array[new_index-2] = '%'
            new_index -= 3
        else:
            # move character
            array[new_index] = array[i]
            new_index -= 1
    return "".join(array)


x = "Mr John Smith    "
print(urlify(x, 13))
