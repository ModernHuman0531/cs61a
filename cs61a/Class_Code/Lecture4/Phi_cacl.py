from math import sqrt
#Self_made function to test the phi
def improve(update,close,guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess
        

def phi_update(guess):
    return 1 + 1 / guess

def phi_close(guess):
    return square_close_to_successor(guess * guess , guess + 1)

def square_close_to_successor(num1 , num2 , tolerance = 1e-15):
    return abs(num1 - num2) < tolerance

#Test our phi caculate
phi = 1 / 2 + sqrt(5) / 2
def test_phi():
    approx_phi = improve(phi_update , phi_close)
    assert(phi , approx_phi), 'phi differs from its approximation'