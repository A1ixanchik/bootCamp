# Заядлый турист ведет тщательный учет своих походов. Во время последнего похода, который занял ровно шаги, за каждым шагом отмечалось, был ли это подъем в гору ,, или спуск ,шаг. Походы всегда начинаются и заканчиваются на уровне моря, и каждый шаг вверх или вниз представляет собойизменение единицы высоты. Мы определяем следующие термины:
# Гора – это последовательность последовательных ступенек над уровнем моря, начиная со ступеньки вверх от уровня моря и заканчивая ступенькой вниз до уровня моря.
# Долина — это последовательность последовательных ступеней ниже уровня моря, начиная со ступеньки вниз от уровня моря и заканчивая ступенькой вверх до уровня моря.
# Зная последовательность подъемов и спусков во время похода, найдите и выведите количество пройденных долин .



# пример 1:
# userSteps = input('enter your steps: ')
# dolina = 0
# sea_level = 0
# for steps in userSteps:
#     if steps == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1
#     else:
#         dolina -=1

# print(f'dolina: {dolina}')


'''Напишите функцию, принимающую на вход длины двух катетов прямо-
угольного треугольника и возвращающую длину гипотенузы, рассчитан-
ную по теореме Пифагора. В главной программе должен осуществляться
запрос длин сторон у пользователя, вызов функции и вывод на экран
по'''
# katet = int(input('Enter a first katet: '))
# katet2 = int(input('Enter a second katet: '))
# def gipotenuza(k1, k2):
#     c = k1 **2 + k2 **2
#     print(pow(c,0.05))

# gipotenuza(katet, katet2)


'''Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси. В основной программе должен демонстрироваться результат
вызова функции.'''

# customer = float(input('Введите длину проезда: '))

# def sum_of_taxi(cust):
#     res = (cust / 0.14) * 0.25 + 4
#     return res

# print(sum_of_taxi(customer))

'''Интернет-магазин предоставляет услугу экспресс-доставки для части
своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
последующие. Напишите функцию, принимающую в качестве единствен-
ного параметра количество товаров в заказе и возвращающую общую
сумму доставки. В основной программе должны производиться запрос
количест­ва позиций в заказе у пользователя и отображаться на экране
'''
# user1 = int(input('What do you wanna order? '))
# def deliver(quantaty): 
#     return (quantaty - 1) * 2.95 + 10.95

# print(deliver(user1))


  

'''Напишите функцию, которая будет принимать на вход три числа в качест­
ве параметров и возвращать их медиану. В основной программе должен
производиться запрос к пользователю на предмет ввода трех чисел, а так-
же вызов функции и отображение результата.'''
# user1 = int(input('Enter a first digit: '))
# user2 = int(input('Enter a second digit: '))
# user3 = int(input('Enter a third digit: '))

# def mediana(first, second, third):
#     if first > second and first < third:
#         print(f'Медиана этих чисел: {first}')

#     elif second > first and second < third:
#         print(f'Медиана этих чисел: {second}')

#     elif third > first and third < second:
#         print(f'Медиана этих чисол: {third}') 

# mediana(user1, user2, user3)


'''Используя решения из упражнений 100 и 102, напишите программу, ге-
нерирующую случайный надежный пароль и выводящую его на экран.
Посчитайте, с какого раза удастся создать пароль, отвечающий нашим
требованиям надежности, и выведите на экран количество попыток. Им-
портируйте функции из предыдущих упражнений и вызывайте их при
необходимости для решения этой задачи.'''
# def validate(password):
#     # password = input('Enter your password: ')
#     if len(password) < 8:
#         print('Your password is too short!')
#     elif not any (cahr.isupper() for cahr in password):
#         print ('Your password must contain at least one uppercase letter!')
#     elif not any (cahr.islower() for cahr in password):
#         print ('Your password must contain at least one lowercase letter!')
#     elif not any (cahr.isdigit() for cahr in password):
#         print ('Your password must contain at least one digit!')
#     elif not any (cahr in '!@#$%^&*()_-+=<>?/' for cahr in password):
#         print ('Your password must contain at least one special character!')
#     else:
#         print('Your password is accepted!')
#         return True



# import secrets
# import string
# import random

# def createPassword():
#     letters = string.ascii_letters
#     digits = string.digits
#     special_chars = string.punctuation
#     selection_list = letters + digits + special_chars
#     strong_password = ''

#     for i in range(10):
#         strong_password = strong_password + ''.join(secrets.choice(selection_list))
#     return strong_password
        
   

# createPassword()
# count = 0

# while True:
#     a = validate(createPassword())
#     count += 1
#     if a == True:
#         break

# print(count, createPassword())

# 1
# Создать функцию, которая будет принимать 3 числа в качестве аргументов, функция должна возвращать сумму первых двух чисел разделеную на третье число
# нужно реализовать проверку на то, что третье число не является нулем, если это ноль, то просто возвратить результат сложения первого и второго числа
# user1 = int(input('first nunmber: '))
# user2 = int(input('second number: '))
# user3 = int(input('third number: '))
# def sum(first, second, third):
#     try:
#         num = (first + second) / third
#     except ZeroDivisionError:
#         num  = first + second

    # return num


# print(sum(user1,user2,user3))

# 2
# Создать фуункцию, которая принимает в качестве аргумента список со строками и в каком регистре нужно вернуть данные, строки могут быть записаны в любом регистре, задача: на основе выбора регистра, возвращать либо список со строками в верхнем регистре, либо в нижнем регистре
# Например: func(["hEllo", "wORld"], "lower") -> ["hello", "world"]
# def list1(small,registr):
#     new_list = []
#     for i in small:
#         if registr == 'lower':
#             new_list.append(i.lower())
#         else:
#              new_list.append(i.upper())
#     return new_list

    
        
# print(list1(['heLLO WORLD'], 'upper'))

# Создать функцию, которая будет принимать в качестве аргумента строку, а затем говорить сколько в ней и каких символов, результать вернуть в виде объекта
# Например: 'Hello' -> {'H': 1, 'e': 1, 'l': 2, 'o': 1}

# user1 = input('Введите ваше слово: ')
# user2 = input('Введите ваше слово: ')

# def transform(coun):
#     dict_ = {x:coun.count(x) for x in coun}
#     dict_2 = {}
#     return dict_


 
# def transforf

# Создать калькулятор используя функции, должны быть доступны операции(+, -, /, *), также должна быть функция-менеджер, которая будет принимать 2 числа и операцию, а затем вызывать нужную функцию и возвращать результат
# user1 = int(input('Введите первое число: '))
# oper = input('Введите оператор: ')
# user2 = int(input('Введите второе число: '))

# def culc(first, op, second):
#     if op == '*':
#           print(f'Результат уможения: {first * second}')
#     elif op == '+':
#          print(f'Результат сложение: {first + second}')
#     elif op == '/':
#          print(f'Результат деление: {first / second}')
#     elif op == '+':
#          print(f'Результат вычетания: {first - second}')
#     else:
#          print('Вы ввели неправильный оператор!!')


# culc(user1, oper, user2)
    



        
# Создайте функцию, которая будет рассылать сообщения пользователям, сообщая о акции в магазине компьютерной техники, отправлять сообщения нужно только тем людям, которые тем или иным образом относятся к IT-сфере
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Hel\'ga', 'age': 35, 'work': 'IT-HR' }
# ]
# def messanger(users):
#     discounts = 'у нас акции на ноутбуки!!'
#     for i in users:
#         for key, value in i.items():
#             if type(value) != int:
#                 if value.startswith('IT'):
#                     print(i['name'], discounts)

# messanger(users)
# Создать функцию, которая будет рассчитывать расход топлива автомобиля, будет принимать 2 аргумента 1-й сколько всего километров проехали, второй сколько понадобилось топлива на это, затем функция должна рассчитать сколько ушло топлива на 100 км и вернуть результат вида: 'На 100км было расходовано 10л горючего'
# user1 = int(input('Сколько километров вы прошли? '))
# def automobile(ras, how):
#     return ras // how

# print(f'На {user1}км было расходовано {automobile(user1, 10)}л топлива')



# Создать функцию, которая будет принимать в качестве аргумента 2 строки, 1-я строка должна быть следующего вида -> '1200m', вторая строка состоит из величины, в которую необходимо преобразовать данные -> 'km', 'cm', 'mm', задача: реализовать логику, которая будет принимать например строку вида '2000m', и строку в которую нужно преобразовать величину например 'km', вывод должен быть '2km'

# user1 = int(input(f'Вводите расстояние метров: '))
# user2 = input('Введите на что вы хотите преобразовать: ')
# def reverser(long, rev):
#     if rev == 'km':
#         print(f'Ваше растояние равняется: {long // 1000} km')
#     elif rev  == 'cm':
#         print(f'Ваше растояние равняется: {long * 100000}cm')
#     else:
#         print(f'Ваше растояние равняется: {long * 1000000}mm')

        
# reverser(user1, user2)

# Расчет премии сотрудникам
# salary- это заработная плата в месяц, overTime- количество часов, которое сотрудник взял сверхурочно, задача: создать функцию, которая будет добавлять к основной зарплате сверхурочное время(1час=200$), функция должна принимать список со словарями и возвращать также список, но уже с измененными данными пример: [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> [{'name': 'Jack', 'salary': 10800}]

# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]


# def overTime(employees):
#     result = []

#     for employer in employees:
#         new_salary = {}

#         for key, value in employer.items():
#             if key == 'name':
#                 new_salary['name'] = value
#             elif key == 'salary':
#                 new_salary['salary'] = value
#             else:
#                 new_salary['salary'] += value * 200

#         result.append(new_salary)
            
#     return result
            
            
# print(overTime(employees))

# Создать функцию, которая в качестве аргумента будет принимать список со строками и числами, задача, отсортировать числа в отдельный список, а строки в отдельный и распечатать оба списка
# ls = [2345, 5678, 6789, 6789, 'Alihan', 12, 'Kurmanbek', 1968, 'Venera', 1969]

# def sorted(ls):
#     ls_of_strings = []
#     ls_of_numbers = []

#     for i in ls:
#         if str == type(i):
#             ls_of_strings.append(i)
#         elif int == type(i):
#             ls_of_numbers.append(i)
#     return ls_of_numbers, ls_of_strings


# print(sorted(ls))


# Создайте функцию, которая будет в качестве аргумента принимать список такого вида как указан выше, и будет возвращать отсортированный список (сортировать по убыванию оценок, используйте sort())
# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def sort(students):
#     return sorted(students, key=lambda a: a['marks'], reverse=True)
    
# print(sort(students))

11
# Создайте функцию, которая будет принимать строку, а затем будет смотреть на все товары и возвращать только те, у которых в названии есть данная строка (учесть, что название может быть полным, а может быть частичным)


# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]

# user = input('Напишите что вы ищете? ')
# def search_product(search,user):
    
#     for i in search:
#         for key, value in i.items():
#             if type(value) != int:
#                 if user in value:
#                     print(f'Ваш продукт найден {i}')

    

# print(search_product(products, user))


# Используя из предыдущей задачи список с товарами, реализовать фильтрацию по категориям, функция должна в качестве аргумента принимать строку с категорией и возвращать список, в котором будут только те товары, у которых категория полностью совпадает с переданной
# 
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]


# user = input('Введите котегорию: ')
# def ret_categories(categories):
#     categorie_list = []
#     for i in products:
#         for key,values in i.items():
#             if type(values) != int:
#                 if values == categories:
#                     categorie_list.append(i)
#     return categorie_list


# print(ret_categories(user))



# Создать счетчик расходов, есть некая переменная, которая будет хранить данные о вашем балансе, создать две функции, первая будет записывать расходы, вторая просто пополнять баланс, первая функция: ее основная задача получать 2 аргумента на что потрачено и сколько потрачено, дальше формировать словарь типа: {'target': 'Products', 'spend': 400}, затем сохранять эти данные в список и соответственно вычитать из баланса сумму трат, вторая функция просто получает в качестве аргумента сумму, которую нужно добавить на баланс, также необходимо реализовать проверку, достаточно ли средств на балансе для совершения расходов


# 1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) число и выводит на окно терминала через команду print(). Далее создайте декоратор, который журналирует это событие. То есть функция декоратор должна писать в dict() предложение: «Функция …………… была запущена успешно», а ключом будет уникальный идентификатор (id).   (10 баллов)
# import random 
# def dec(func):
#     def wrapper(*args, **kwargs):
#         print(f'Функция {func.__name__} была запущена успешно')
#         return func()
#     return wrapper


# @dec
# def generate():
#     digit = random.randint(0,100)
#     print(digit) 

# generate()


# # 2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# # Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и т.п. (10 баллов)
# user = input('Введите слово: ').upper().split()
# # def phrase(phrases):
# #     # res = ''.join([i[0] for i in phrases])
# #     # # for i in phrases:
# #     # #     res.append(i[0])
# #     # return res

# # print(phrase(user))                [1, 2, 3, 55]   
# # a = ''.join(list(map(lambda x: x[0],user)))
# # print(a)

        
    
# # 3) '''Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов.''' (15 баллов)

# def dec(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except:
#             return('Были введены неправильные данные')
#     return wrapper

# @dec
# def distinct(*args):
#     return sum(args)

# print(distinct(2134, '4321'))

# 4) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,''' (15 баллов)
# def dec(func):
#     def wrapper(*args, **kwargs):
#         print(type(func(*args, **kwargs)))
#         print(type(int(func(*args, **kwargs))))

#     return wrapper
# user = input('Введите данные: ')


# @dec
# def ret_func(a):
#     return a

# ret_func(user)    



# 5) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.''' (20 баллов)
# def dec(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         if count < 3:
#             func()
#             count += 1
#         else:
#             print('Максимальное количество вызовов функции 3')
#     return wrapper
        
        

# @dec
# def limit():
#     print('poka limita net!!')
# limit()
# limit()
# limit()
# limit()


# 6) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.'''
# def dec(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return 'Нельза умножить такой тип данных на integer'
#     return wrapper

# user1 = int(input('Введите первое число: '))
# user2 = int(input('Введите второе число: '))    
# @dec

# def sum_of_num(*args):
#     return sum(args)

# print(sum_of_num(user1, user2))

# 1)Дано: переменная 

# Необходимо вывести сумму цифр, представленных в виде одного строкового значения '123456789'. Сумма этих цифр составляет 45. Напишите код, который выдаст эту её.
# Подсказка: используйте генератор списка, функцию int(), функцию sum() для суммирования списка, состоящего из чисел.
# digits = '123456789'
# def sun(a):
#     sum = 0
#     for digit in digits:
#         sum += int(digit)
#     return sum
# print(sun(sum))


# 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.''' 
# dict_ = [
#     {
#     'name': 'John Snow',
#     'role': 'Admin',
#     },
    
#     {
#     'name': 'Raychel',
#     'role': 'User',
#     },
#     {
#     'name': 'Alihan',
#     'role': 'User',
#     }
# ]
# def dec(func):
#     names = ['ali', 'jake']
    
#     def wrapper(*args, **kwargs):
#         name = input('Введите ваще имя: ')
#         role = input('Введите вашу роль: ')
#         if name in names:
#             print(func(*args, **kwargs))
#         else:
#             raise('asddasd')

#         # for i in args:
#         #     for x in i:
#         #         for y in x.items():
#         #             if role in y:
#         #                 return ('Welcome')
#         #             else:
#         #                 print ('Sory you don\'t have permession!')
                
#     return wrapper


# @dec
# def permession(*args):
#     return args

# print(permession('dict_'))
 

# #  1)Дано: переменная 
# digits = '123456789'
# def translate(dig):
#     count = 0
#     for i in dig:
#         count += int(i)
#     return count

# print(translate(digits))


# Необходимо вывести сумму цифр, представленных в виде одного строкового значения '123456789'. Сумма этих цифр составляет 45. Напишите код, который выдаст эту её.
# Подсказка: используйте генератор списка, функцию int(), функцию sum() для суммирования списка, состоящего из чисел.


# 2) напишите лямбда функцию
# которая принимает одно число, и возводит его в квадрат
# user = int(input('Введите ваще число: '))
# x = lambda a: a ** 2
# print(x(user))





# 3) напишите лямбда функцию которая принимает 2 числа, первое число возводите в степень второго числа
# user = int(input('Введите первую цифру: '))
# user2 = int(input('Введите вторую цифру: '))
# res = lambda x, y: pow(x, y)
# print(res(user, user2))




# 4) напишите лямбда функцию 
# которая принимает список имён, и функция должна приветствовать все имена (используйте функцию map)

ls = ['Alihan', 'Kurmanbek', 'Venera', 'Farida', 'Farhat']
res = list(map(lambda x:'Hello Mr/Mrs ' + x, ls))
print(res)

# 5) напишите лямбда функцию 
# которая принимает список чисел, и она будет фильтровать этот список,
#  то есть будет принимать только те числа которые делятся на 5, использовать встроенные функции filter, list
num = [12, 134, 214, 3241, 3241, 4321,25]
res = list(filter(lambda x: x % 5 == 0,num))
print(res)





'''Магическими называются даты, в которых произведение дня и месяца
составляет последние две цифры года. Например, 10 июня 1960 года –
магическая дата, поскольку 10 ´ 6 = 60. Напишите функцию, определя-
ющую, является ли введенная дата магической. Используйте написан-
ную функцию в главной программе для отображения всех магических
дат в XX ве­ке.'''


# user = input('Введите даты: ' ).split()

# res = int(user[0]) * int(user[1])
# res2 = int(user[-1][2:])
# if res == res2:
#     print(f'{user}, магическое число!!')
# else:
#     print('Не магическое!!')


#

'''Напишите функцию для определения количества дней в конкретном ме-
сяце. Ваша функция должна принимать два параметра: номер месяца
в виде целого числа в диапазоне от 1 до 12 и год, состоящий из четырех
цифр. Убедитесь, что функция корректно обрабатывает февраль високос-
ного года. В основной программе запросите у пользователя номер месяца
и год и отобразите на экране количество дней в указанном месяце.'''
# user = int(input('Введите номер месяца: '))
# user2 = int(input('Введите год: '))
# def days_of_months(month, year):

#     if month == 2 and year % 4 != 0:
#         print(f'Ваш {year} не является висококосным и вашем месяце {28} дней')
#     elif month == 2 and year % 4 == 0:
#         print(f'Ваш {year}, является високосным!')
#     elif month == 1:
#         print(f'Вашем месяце {month * 31} дней!')
#     elif month == 3:
#         print(f'Вашем месяце 31 дней!')
#     elif month == 4:
#         print(f'Вашем месяце {30} дней!')
#     elif month == 5:
#         print(f'Вашем месяце {30} дней!')
#     elif month == 6:
#         print(f'Вашем месяце {31} дней!')
#     elif month == 7:
#         print(f'Вашем месяце {30} дней!')
#     elif month == 8:
#         print(f'Вашем месяце {31} дней!')
#     elif month == 9:
#         print(f'Вашем месяце {31} дней!')
#     elif month == 10:
#         print(f'Вашем месяце {30} дней!')
#     elif month == 11:
#         print(f'Вашем месяце {31} дней!')
#     elif month == 12:
#         print(f'Вашем месяце {30} дней!')
#     return month, year

# days_of_months(user, user2)
#

'''Напишите две функции с именами hex2int и int2hex для конвертации
значений из шестнадцатеричной системы счисления (0, 1, 2, 3, 4, 5, 6, 7,
8, 9, A, B, C, D, E и F) в десятичную (по основанию 10) и обратно. Функ-
ция hex2int должна принимать на вход строку с единственным символом
в шестнадцатеричной системе и преобразовывать его в число от нуля
до 15 в десятичной системе, тогда как функция int2hex будет выполнять
обратное действие – принимать десятичное число из диапазона от 0 до
15 и возвращать шестнадцатеричный эквивалент. Обе функции должны
принимать единственный параметр со входным значением и возвращать
преобразованное число. Удостоверьтесь, что функция hex2int корректно
обрабатывает буквы в верхнем и нижнем регистрах. Если введенное поль-
зователем значение выходит за допустимые границы, вы должны вывести
сообщение об ошибке.'''
# dict_ = {
#     'A': 10,
#     'B': 11,
#     'C': 12,
#     'D': 13,
#     'E': 14,
#     'F': 15

# }
# def hex2int():
#     user = input('Введите ваше число: ').upper()[::-1]
#     counter = 0
#     ls = []
#     for i in user:
#         if i.isdigit():
#             ls.append(counter * 16 * int(i) )
#         else:
#             ls.append(counter * 16 * dict_[i] )
#         counter += 1
#     return sum(ls) + 10
# print(hex2int())

# def int2hex():
#     user = int(input('Введите число: '))
#     ls = []
#     while True:
#         if user == 0:
#             break
#         ls.append(user % 16)
#         user = user // 16
#     return ls[::-1]

# print(int2hex())
 
#

'''Представьте, что в вашем регионе устаревшим является формат номер-
ных автомобильных знаков из трех букв, следом за которыми идут три
цифры. Когда все номера такого шаблона закончились, было решено об-
новить формат, поставив в начало четыре цифры, а за ними три буквы.
Напишите функцию, которая будет генерировать случайный номерной
знак. При этом номера в старом и новом форматах должны создаваться
примерно с одинаковой вероятностью. В основной программе нужно сге-
нерировать и вывести на экран случайный номерной знак.'''
from random import randint, choice 
import string
def generator():
    letters = string.ascii_letters
    letters = [i for i in letters]
    
    numbers = [choice(letters) for x in range(1,4)] + [choice([1,2,3,4,5,6,7,8,9,10]) for i in range(1,4)]
    numbers1 = [choice([1,2,3,4,5,6,7,8,9,10]) for i in range(1,5)] + numbers[:3]
    return numbers, numbers1

print(generator())



        
    











