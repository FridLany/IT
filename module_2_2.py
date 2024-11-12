first = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
forward = int(input('Введите третье число:'))

if first == second == forward:
    print('Вывод: 3')
elif first == second or second == forward or first == forward:
    print('Вывод: 2')
else:
    print('Вывод: 0')