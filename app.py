def minimumBribes(q):
    n = len(q)
    bribes = 0
    for i in range(n):
        if q[i] > i+1:
            x = q[i] - i - 1
            if x > 2:
                print("Too chaotic")
                return
            bribes += x

    print(bribes)


x = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(x)
