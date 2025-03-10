import math


def square(side):
    area = side ** 2
    return math.ceil(area) if not isinstance(side, int) else area


side = float(input("Длина стороны квадрата: "))
result = square(side)
print(f'Округленная в большую сторону площадь квадрата - {result}')
