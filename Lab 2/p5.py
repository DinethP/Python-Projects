import math


def check_valid(rectangle):
    if (rectangle[0] > 0 and rectangle[1] > 0):
        return True
    else:
        return False


def is_square(rectangle):
    if rectangle[0] == rectangle[1]:
        return True
    else:
        return False


def diagonal_len(rectangle):
    return math.sqrt(rectangle[0] * rectangle[0] + rectangle[1] * rectangle[1])


def height(rectangle):
    return rectangle[0]


def width(rectangle):
    return rectangle[1]


def area(rectangle):
    return rectangle[0] * rectangle[1]


def perimeter(rectangle):
    return 2*rectangle[0] + 2*rectangle[1]
