def fib(n):# This is lack of effiency because of we have to count the same result repeatedly
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#In order to prevent us from counting the same stuff repeatedly, we can build a function that help us memory the result that we have already count
def memo(f):
    cache = {}#Dictionary can imagine as map in c++
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized
