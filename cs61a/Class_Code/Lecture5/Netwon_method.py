#Newton's Method is suited for any function to find the root of the function , as long as the function can be differentiate
def improve(update , close , guess = 1):#improve program is just the program keeps improving the answer
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(num1 , num2 , tolerance = 0.001):
    return abs(num1 - num2) < tolerance

def newton_update(f , df):
    def update(x):
        return x - f(x) / df(x)
    return update


def close_to_zero(f , df):
    def near_zero(x):
        return approx_eq(f(x) , 0)
    return improve(newton_update(f , df) , near_zero)

def Calculate_square(a):#find the root of x^2  = a
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return close_to_zero(f , df)

def power_of_x(x , n):
    product , num = 1 , 0
    while num < n:
        product , num = product * x , num + 1
    return product

def nth_root_of_a(a , n):
    def f(x):
        return power_of_x(x , n) - a
    def df(x):
        return power_of_x(x , n - 1) * n
    return close_to_zero(f , df)
    

y = nth_root_of_a(125 , 3)
print(y)
         