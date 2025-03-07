import math


print('Введите коэффициенты a, b, c для уравнения ax^2 + bx + c = 0')
a = float(input('Введите a -> '))
b = float(input('Введите b -> '))
c = float(input('Введите c -> '))

discriminant = b * b - 4 * a * c

if discriminant > 0:
    root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    result = f'Корни уравнения: {root_1} и {root_2}'

elif discriminant == 0:
    root = -b / (2 * a)
    result = f'Единственный корень уравнения: {root}'

else:
    result = 'У уравнения нет действительных корней'

print(result)