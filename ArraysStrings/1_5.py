# Given two strings S and T, determine if they are both one edit distance apart.
def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    N = min(len(s1), len(s2))

    mismatch = False
    index1 = 0
    index2 = 0

    for i in range(N):
        if s1[index1] != s2[index2]:
            if mismatch:
                return False

            if len(s1) == len(s2):
                index1 += 1
                index2 += 1

            elif len(s1) == N:
                index2 += 1
            else:
                index1 += 1

            mismatch = True
        else:
            index1 += 1
            index2 += 1

    return True
