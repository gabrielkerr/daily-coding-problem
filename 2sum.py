"""
Solution to 2 sum problem from dailycodingproblem.com
"""


def two_sum(l, k, count, cache):

    if count > 2:
        return False

    if k == 0:
        return True

    if k < 0:
        return False

    sorted_l = sorted(l)
    sorted_l.append(k)
    t = tuple(sorted_l)
    if t in cache.keys():
        return cache[t]

    has_soln = True

    for i in range(len(l)):
        curr = l[i]
        val = has_soln and two_sum([x for x in l if x != curr], k-curr, count+1, cache)
        if val:
            break

    cache[t] = val
    return val


if __name__ == '__main__':
    l = [10, 15, 3, 7]
    k = 17
    k2 = 11
    cache = {}
    cache2 = {}
    print(two_sum(l, k, 0, cache))
    print(two_sum(l, k2, 0, cache2))
