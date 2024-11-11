from math import gcd
class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)
    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    
    """Define the function that can add the Ratio object together"""
    def __add__(self, other):
        #other is ratio object
        if isinstance(other, Ratio):
            numer = self.numer * other.denom + self.denom + other.numer
            denom = self.denom * other.denom
        #other is integer
        elif isinstance(other, int):
            numer = self.numer + other * self,denom
            denom = self.denom
        g = gcd(numer, denom)
        return Ratio(numer//g, denom//g)
    __radd__ = __add__
        