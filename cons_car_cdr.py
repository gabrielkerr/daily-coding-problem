"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""


# Returns a function that takes another function
# in the form f(a, b)
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair_func):
    def get_first(a, b):
        return a
    return pair_func(get_first)



def cdr(pair_func):
    def get_last(a, b):
        return b
    return pair_func(get_last)


if __name__ == '__main__':
    print("car(cons(3, 4) =", car(cons(3, 4)))
    print("cdr(cons(3, 4) =", cdr(cons(3, 4)))
