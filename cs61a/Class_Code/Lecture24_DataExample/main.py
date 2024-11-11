def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    # Find the minimum absolute value
    min_abs = min(map(abs,s))
    return [i for i in range(len(s)) if s[i] == min_abs]
def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.

    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    #sum = s[index] + s[index+2], if index + 2 >= len(s), then return max
    #----------------------------My code-------------------------------------
    max = -100000000
    for i in range(len(s)):
        if i + 1 >= len(s):
            return max
        else:
            num = s[i] + s[i+1]
            if num > max:
                max = num

def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.

    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    #create a dict key that iterate from 0 to 9, but if dict key dosen't exist in s's last digit, then we don't want it
    last_digits = [x % 10 for x in s]
    return {d:[x for x in s if x % 10 == d] for d in range(10) if d in last_digits}

def all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """    
    while len(s) > 1:
        num = s[0]
        if num in s[1:]:
            return True
        s = s[1:]
    return False
    #return all(s[i] in s[:i]+s[i+1:] for i in range(len(s)))
class Link:
    """A linked list.

    >>> Link(1, Link(2, Link(3)))
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> s
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(s)
    <1 <2 3> 4>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def merge(s, t):
    """Return a sorted Link containing the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """
    # 1. Sort the situation with if there is only first, s.first <= t.first , and s.first > t.first
    #2. Do the recursion
    if s.rest is Link.empty:
        return t
    elif t.rest is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first,merge(s.rest, t))
    else:
        return Link(t.first, merge(s,t.rest))


def merge_in_place(s, t):
    """Return a sorted Link containing the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge_in_place(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(1, Link(4, Link(5))))
    >>> b
    Link(1, Link(4, Link(5)))
    """
    # The idea is quite similar to merge but instead of create a new link, but we don't create a new link but modify the original link
    if s.rest is Link.empty:
        return t
    elif t.rest is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge(s.rest, t)
        return s
    else:
        t.rest = merge(s, t.rest)
        return t