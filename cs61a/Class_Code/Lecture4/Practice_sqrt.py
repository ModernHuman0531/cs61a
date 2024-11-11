def search(f):#if function search the value , will return x, else will keep running
    x = 0
    while True:
        if f(x):
            return x
        else:
            x += 1
    
def square(x):
    return x * x

def inverse(f):#enable to find the reverse function
    return lambda y:search(lambda x: f(x) == y ) #Input y , use search function to find the x value until x has value, if don't find x will in the infinte loop

sqrt = inverse(square)
