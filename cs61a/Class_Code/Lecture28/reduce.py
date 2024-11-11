from operator import add ,mul, truediv
def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.
    ex: reduce(mul, [2, 4, 6, 8], 1) is equivalent to mul 8, (mul 6, (4, mul(1, 2)))
    >>> reduce(mul, [2, 4, 6, 8], 1)
    384
    """
    if len(s) == 0:
        return initial
    else:
        initial = f(s[0], initial)
        return reduce(f, s[1:], initial)
    
def divide_all(n, ds):
    #Have to 'handle' the situation when the list of ds have one element that is 0
    try:
        reduce(truediv, n, ds)
    except ZeroDivisionError as e:
        return ('inf')
    #Best benefit of writing this way is that the reduce function don't have to deal with ZeroDivisionError