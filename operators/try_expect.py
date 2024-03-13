# оброботка исключений 
# Операторы try ... expect
# ошибки бывают двух типов - синтакс ошибки связанные с кодом 

# SyntaxError
# IndentationError
# TabError

# Исключение Exceptions -> связяны с неправильным данными которые передаются в код, операции
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# IndexError
# ValueError
# BaseException  прородитель всех исключений
# try:
    
# except:
#     print('Invalid Values!')
# try:
#     num = int(input('Enter a number: '))
#     num2 = int(input('Enter the number2: '))
#     print(f'{num} / {num2} = {num / num2}')
# except ValueError:
#     print('Чувак ты ввел неправильные данные для функции int!')
# except ZeroDivisionError:
#     print('На ноль делить нельза!')


# # print('Очень важный код')

# # try:
# #     <body> код с вероятным исключением 
# # except: 
# #     <body except> сработает только если ошибка в try 
# # <else>:
# #      <body> сработает только если нет ошибки в try 
# # <Finally>:
# #      <body> сработает в любом случае 

# dict_ = {
#     1: 'One',
#     2: 'Two', 
#     3: 'Three'
# }
# try:
#     key = int(input('Enter the key: '))
#     print(dict_)
# except ValueError:
#     print('Invalid value for key!')
# except KeyError:
#     print('Key does not exists!')
# else: 
#     print('No errors!')
# finally:
#     print('The end!')




    # ------------------------------------
# Отаброжение ошибки
# 1. import sys  
# import sys
# ls = [1, 2, 3, 4, 5]
# try: 
    # index = int(input('Enter the index: '))
    # print(ls[index])
# except:
#     print(f'Oops, we catched {sys.exc_info()[1]} error!')



# 2. Exeption as <name(e)>
ls = [1, 2, 3, 4, 5]
while True:
    try:
        index = int(input('Enter the index: '))
        print(ls[index])
    except Exception as e:
        print(f'Ops, we catched {e.__class__}error!')





