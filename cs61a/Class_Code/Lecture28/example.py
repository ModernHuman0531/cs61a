def invert(x):
    y = 1/x # When x = 0 goes here, it never will have a chance to execute the following code, because it has ZeroDivisionError
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:# 1.Will first run the body in the try function, if the function face the 'ZeroDivisionError'
        return invert(x)
    except ZeroDivisionError as e:#2. Then will directly run this line, and use 'as' to give parameter 'e' with ZeroDivisionError
        print('handled ', e)
        return 0
