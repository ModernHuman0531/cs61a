from operator import mul, sub, add, truediv
def square(x):
    return x*x
def identity(x):
    return x
def accumualte(combiner, start, n, term):
    def helper(combiner, start,num,term):
        if num > n:
            return start
        else:
            start, num = combiner(start, term(num)), num+1
            return helper(combiner, start,num,term)
    return helper(combiner, start, 1, term)