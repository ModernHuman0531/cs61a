"""Use data abstractin to represent rational numbers.
1.Use constructor called rational(nume, deno) to create a rational number named x.
2.Use function numerator(x) to get the numerator of x.
3.Use function denominator(x) to get the denominator of x.

"""
from math import gcd

def rational(numer,denom):
    """Create a rational number x with numerator numer and denominator denom."""
    g = gcd(numer,denom)
    if g == 1:
        return [numer,denom] #construct a rational number to store the numerator and denomnator into a list
    else:
        return [numer//g , denom//g]

def numerator(x):
    return x[0]

def denominator(x):
    return x[1]

def rational_multiply(x1 , x2):
    return rational((numerator(x1) * numerator(x2)) , (denominator(x1) * denominator(x2)))

def add_rational(x1 , x2):
    return rational((numerator(x1) * denominator(x2) + numerator(x2) * denominator(x1)) , (denominator(x1) * denominator(x2)))

def print_rational(x):
    print(numerator(x) + '/' + denominator(x))