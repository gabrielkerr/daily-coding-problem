"""
Solution to 2 sum problem from dailycodingproblem.com
"""


def two_sum(l, k):
    m = [0]*(max(l) + 1)

    for x in l:
        m[x] += 1

    for x in l:
        if k-x == x and m[k-x] >= 2:
            return True

        if m[k-x] != 0:
            return True

    return False


if __name__ == '__main__':
    l = [10, 15, 3, 7]
    k = 17
    k2 = 11
    print(two_sum(l, k))
    print(two_sum(l, k2))
