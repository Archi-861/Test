
print('Выберите опцию:\n')

choice = int(input(f'1. Конвертировать Цельсий в Фаренгейт\n'
                   f'2. Конвертировать Фаренгейт в Цельсий\n'
                   f'Ваш выбор -> '))


if choice == 1:
    celsius = float(input('Введите температуру в градусах Цельсия: '))
    farenheit = (celsius * 9 / 5) + 32
    print(f'Температура в градусах Фаренгейта: {farenheit}')

elif choice == 2:
    farenheit = float(input('Введите температуру в градусах Фаренгейта: '))
    celsius = (farenheit - 32) * 5 / 9
    print(f'Температура в градусах Цельсия: {celsius}')

else:
    print('Неправильный выбор')
