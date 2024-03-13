# senctence = input('write down a sentene: ')
# res = 'Yes, voprositel\'noye!'if senctence[-1] == '?' else 'normal one'
# print(res)

# Ternary operators(Тернарный оператор) - это конструкция которая по своему действию аналогична if/else, но при этом записывается в одну строчку

# number = int(input('Enter a digit: '))
# print('even number' if number % 2 == 0 else 'odd number')
# if senctence[-1] == '?':
#     print('Yes, voprositel\'noye!')
# else:
#     print('Normal one!')
# ls = [55, 65, 75, 89, 100, 15, 6]
# choice =input('Vvedite max/min: ').lower().strip()
# res = max(ls) if choice == 'max' else min(ls) if choice == 'min' else 'Invalid operator!'
# print(res)

flag = True

symbols = '0123456789' + '-' + '.'
while flag:
    num1 = input('Enter a digit: ')
    is_correct = True
    for x in num1:
        if x not in symbols:
            print('Вы ввели некоректное число!')
            is_correct = False
            break
    if not is_correct:
        continue
        
    num2 = input('Enter a digit second: ')
    is_correct = True
    for x in num2:
        if x not in symbols:
            print('Вы ввели некоректное число!')
            is_correct = False
            break
    if not is_correct:
        continue

    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    operator = input('enter a operation /*/ /+/ /-/ (/): ')
    if operator == '+':
        print(f'Результат: {num1 + num2}')
    elif operator == '-':
        print(f'Result: {num1 - num2}')
    elif operator == '*':
        print(f'Result: {num1 * num2}')
    elif operator == '/':
        print(f'Result: {num1 / num2}') if num2 != 0 else 'На ноль делить нельза!'


    else:
        print('Вы ввели неправильный оператор!')
    

    choice = input('Хотите продолжить (yes/no)?: ')
    if choice.lower().strip() != 'yes':
        flag = False
        print('Пока Пока!')

    # print(num1, type(num1)
    # print(num2, type(num2))


