# https://github.com/jack1362/lab11-JL-IS
# Partner 1: Jack Lenhart
# Partner 2: Ishan Sujin

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    else:
        return b / a
def log(a, b):

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")

    return math.log(b, a)

def exponent(a, b):
    return a ** b