# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

import math

def zero(*args):    
    if len(args) == 0:
        return 0
    else:
        return eval(f'math.floor(0 {args[0]})')
def one(*args):     
    if len(args) == 0:
        return 1
    else:
        return eval(f'math.floor(1 {args[0]})')
def two(*args):     
    if len(args) == 0:
        return 2
    else:
        return eval(f'math.floor(2 {args[0]})')
def three(*args):     
    if len(args) == 0:
        return 3
    else:
        return eval(f'math.floor(3 {args[0]})')
def four(*args):     
    if len(args) == 0:
        return 4
    else:
        return eval(f'math.floor(4 {args[0]})')
def five(*args):
    if len(args) == 0:
        return 5
    else:
        return eval(f'math.floor(5 {args[0]})')
def six(*args):     
    if len(args) == 0:
        return 6
    else:
        return eval(f'math.floor(6 {args[0]})')
def seven(*args): 
    if len(args) == 0:
        return 7
    else:
        return eval(f'math.floor(7 {args[0]})')
def eight(*args):     
    if len(args) == 0:
        return 8
    else:
        return eval(f'math.floor(8 {args[0]})')
def nine(*args):     
    if len(args) == 0:
        return 9
    else:
        return eval(f'math.floor(9 {args[0]})')

def plus(x): 
    return f'+ {x}'
def minus(x): 
    return f'- {x}'
def times(x):
    return f'* {x}'
def divided_by(x): 
    return f'/ {x}'