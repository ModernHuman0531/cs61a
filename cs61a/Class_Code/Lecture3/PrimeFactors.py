def prime_factors(n):#This function just display th prime factor of n, each function should just fo one job
    """ Display all the factor of number in non_decreasing order
    >>> prime_factors(6)
    2
    3
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)

def smallest_prime_factor(n):#This function apply the alogrithn of find the smallest prime factor of n
    """Return the smallest prime factor number of n"""
    k = 2
    while n % k != 0:
        k += 1
    return k