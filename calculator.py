#https://github.com/jack1362/lab11-JL-IS.git
#Partner 1: Jack Lenhart
#Partner 2: ishan sujin
import math
# First example
def add(a, b):
    return a + b
def sub(a, b):
    return a-b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    else:
        return b / a
def log(a, b):

    if b < 0:
        raise ValueError()

    if a ==1 or a <= 0:
        raise ValueError()
    return math.log(b, a)

def exp(a, b):
    return a ** b




