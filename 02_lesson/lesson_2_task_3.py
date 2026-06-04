import math


def square(side):
    area = side * side
    return math.ceil(area)


print(f"Площадь квадрата: {square(4.2)}")
