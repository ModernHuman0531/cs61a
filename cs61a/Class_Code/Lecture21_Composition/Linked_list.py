class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        return 'Link({0}, {1})'.format(self.first, self.rest)
    
def range_link(start, rest):
    """return a link containing consecutive integers from start to end.
    
    >>> range_link(3,6)
    Link(3,Link(4,Link(5)))
    """
    if start < rest:
        Link(start, range_link(start + 1,range))
    else:
        rest = Link.empty

def odd(num):
    if num % 2:
        return True
    else:
        return False
      
def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s
    >>> map_link(square, range_link(3,6))
    Link(9,Link(16,Link(25)))
    """
    if s == Link.empty:
        return s
    else:
        first = f(s.first)
        Link(first, map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link that contains only th eelements x of link s for which f(x) is a ture value.
    >>> filter_link(odd, range(3,6))
    Link(3,Link(5))
    """
    if s == Link.empty()
        return s
    else:
        #check the first element, if pass, put it in the link, or check the rest of the link
        rest_link = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, rest_link)
        else:
            return rest_link
        
def add(s, v):
    """Check the s.first to compare with v.Find the first number just bigger than add it to link"""
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first,s.rest)
    elif s.first < v and s.rest is Link.empty():#The v is bigger than all s.first
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest,v)
    return s