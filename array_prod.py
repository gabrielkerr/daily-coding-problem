"""
Given an array, create a new array where each entry i is the product of all elements in the list except i.
Don't use division.
"""

def array_prod(l):
    arr_len = len(l)
    left = [1]*arr_len
    right = [1]*arr_len
    prod = [1]*arr_len

    for i in range(1, arr_len):
        left[i] = left[i-1] * l[i-1]

    for j in range(1, arr_len):
        right[arr_len - 1 - j] = right[arr_len - 1 - j + 1] * l[arr_len - 1 - j + 1]

    for k in range(arr_len):
        prod[k] = left[k] * right[k]

    return prod


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(array_prod(l))
