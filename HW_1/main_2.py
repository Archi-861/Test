import math


print('Введите длины сторон треугольника a, b и c:\n')

a = float(input('Введите сторону a -> '))
b = float(input('Введите сторону b -> '))
c = float(input('Введите сторону c -> '))


if (a + b > c) and (a + c > b) and (b + c > a):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'Площадь треугольника равна {area}')

else:
    print('Такого треугольника не существует')