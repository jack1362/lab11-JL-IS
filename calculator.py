# https://github.com/jack1362/lab11-JL-IS
# Partner 1: Jack Lenhart
# Partner 2: Ishan Sujin

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")

        return math.sqrt(a)
    except ValueError:
        raise ValueError("Invalid square root argument")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except (ValueError, TypeError):
        raise ValueError("Invalid hypotenuse arguments")

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    else:
        return b / a

def exp(a, b):
    return a ** b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")

    return math.log(b, a)