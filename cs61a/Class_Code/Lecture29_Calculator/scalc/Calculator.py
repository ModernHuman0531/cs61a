"""An interpreter fro the Scheme-Syntax Calculator Language

An interpreter for a calculator language that uses prefox-order .
Operator expressions must ber operator symbols. Opreand expression seperated by spaces.

Examples:
> (* 1 2 3)
6
> (+)
> (+ (/ 4 8))
2.5
> (+1
    (-23)
    (* 4 2.5))
-12
> )
SyntaxError: unexpected token: )
> 2.3.4
ValueError: invalid numeral: 2.3.4
> +
TypeError: + is not a number or call expression
> (/ 5):
TypeErrorL / requires exactly 2 arguments
> (/ 1 0)
ZeroDivisionError: division by zero
"""
from ucb import trace, main, interact
from operator import add, sub, mul, truediv
from scheme_reader import Pair, nil, scheme_read, buffer_input

# Eval and Apply
def reduce(f, s, initial):
    if len(s) == 0:
        return initial
    else:
        initial = f(s[0], initial)
        return reduce(f, s[1:], initial)

def calc_eval(exp):
    # Expreesion must be one  of the primitive or call expression
    if type(exp) in (int, float): # Primitive case
        return exp # Just return primitive itself
    elif isinstance(exp, Pair):# ex: (+ 1 2 3)
        arguments = exp.second.map(calc_eval)# (1 2 3)
        return calc_apply(exp.first, arguments)# calc_apply(+, (1 2 3))
    else:
        raise TypeError
    
def calc_apply(operator, args):
    # The operator must be a string like: '+', '-', '*', '/'
    if not isinstance(operator, str):
        raise TypeError(str(operator) + 'is not symbol')
    if operator == '+':
        return reduce(add, args.seconf, args.first)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + 'must have at least 1 argument')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args.second, args.first)
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) == 0:
            raise TypeError(operator + 'must have at least 1 argument')
        elif len(args) == 1:
            return 1/args.first
        else:
            return reduce(truediv, args.second, args.first)
    else:
        raise TypeError(operator + 'is an unkown operator')
        


def read_eval_print_loop():
    """Run a read-eval-print loop for calculator"""
    while True:
        try:
            src = buffer_input() # read text from user
            while src.more_on_line:
                expression = scheme_read(src)# Parse the expression using scheme_read expression
                print(calc_eval(expression))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except(KeyboardInterrupt,EOFError):# <Control D>etc..
            print('Calculation completed.')
            return 

