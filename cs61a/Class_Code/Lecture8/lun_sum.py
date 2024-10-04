def spilt(n):
    return n // 10 , n % 10

def sum_digit(n):
    if n < 10:
        return n
    else:
        number_no_last , last = spilt(n)
        return sum_digit(number_no_last) + last
    
def luhn_sum(n):
    if n < 10:
        return n
    else:
        number_no_last , last = spilt(n)
        return luhn_double_sum(number_no_last) + last
    
def luhn_double_sum(n):
    number_no_last , last = spilt(n)
    luhn_digit = sum_digit(2 * last)    
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(number_no_last) + luhn_digit
    
def luhn_sum_itertation(n):
    double , digit_sum = False , 0
    while n > 0:
        if double:
            digit_sum += sum_digit((n % 10) * 2)
            double = False
        else:
            digit_sum += n % 10
            double = True
        n //= 10
    return digit_sum
