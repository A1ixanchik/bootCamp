# Задача 1. 

# players = {

#     ("Will", "Smith"): (10, 5, 13),

#     ("Bob", "Robbin"): (7, 5, 14),

#     ("Rob", "Bobbin"): (12, 8, 2)

# }
# res = []
# for key,value in players.items():
#     res1 = list(key) + list(value)
#     res.append(tuple(res1))
# print(res)

# Задача 2
# ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# tuple1 = []
# for i in range(0, len(ls), 2):
#     tuple_ = (ls[i], ls[i+1])
#     tuple1.append(tuple_)

# print(tuple1)
# # Задача 3

#  Посчитайте, сколько раз символ "O"и "А" встречается в строке.   
# "ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО НРАВСТВЕННО, НАДО ЗНАТЬ, ЧТО БЕЗНРАВСТВЕННО; ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО ДЕЛАТЬ, НАДО ЗНАТЬ, ЧЕГО НЕ ДОЛЖНО ДЕЛАТЬ"
# str1 = "ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО НРАВСТВЕННО, НАДО ЗНАТЬ, ЧТО БЕЗНРАВСТВЕННО; ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО ДЕЛАТЬ, НАДО ЗНАТЬ, ЧЕГО НЕ ДОЛЖНО ДЕЛАТЬ"
# counterA = 0
# counterO = 0
# print(str1.count('О'),str1.count('А'))

# for i in str1:
#     if i == 'А':
#         counterA = counterA + 1
#     elif i == 'О':
#         counterO = counterO + 1
    
# print(counterO, counterA)


 
        


# Задача 4 

# Переделайте прошлый калькулятор
# Сделайте так, чтобы калькулятор спрашивал постоянно данные для совершения операций в калькулятор

# while True:
#     culc1 = int(input('Enter an integer: '))
#     op = input('Write down a operator: ')
#     culc2 = int(input('Enter an integer: '))
#     if op == '+':
#         print(culc1 + culc2)
#     elif op == '-':
#         print(culc1 - culc2)
#     elif op == '/':
#         print(culc1 / culc2)
#     elif op == '*':
#         print(culc1 * culc2)
#     else:
#         print('Invalid operators!')
    
    


# Если пользователь вводит букву q то калькулятор должен завершаться (для хардкора, если пользователь введет пустую строку, вывести строку "Нет ничего приятнее, чем знание о твоих знаниях!


# Задача 5. (дополнительно)

# Дополнительно: попробуйте реализовать программу через цикл While, "стоп-слово" для выхода из цикла "Выход"

# Мы решили написать приложение для удобного прослушивания музыки, но наши песни хранятся в виде словаря. Каждая песня состоит из названия и продолжительности с точностью до долей минут.

 

# violator_songs = {

#     'World in My Eyes': 4.86,

#     'Sweetest Perfection': 4.43,

#     'Personal Jesus': 4.56,

#     'Halo': 4.9,

#     'Waiting for the Night': 6.07,

#     'Enjoy the Silence': 4.20,

#     'Policy of Truth': 4.76,

#     'Blue Dress': 4.29,

#     'Clean': 5.83

# }

 

# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен, а на экран выводит общее время их звучания.

# listener = int(input('Write down quantity of songs: '))
# duration = 0
# for l in range(listener):
#     music1 = input('название песни: ')
#     if music1 in violator_songs:
#         duration = duration + violator_songs[music1] 

# print(duration)


# Задача 6. (дополнительно)

 

# Асан помимо программирования также увлекается и географией, поэтому он решил связать эти две области и написать для своего проекта небольшую программу-навигатор.

 

# Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся, в одну строку. Затем пользователь вводит три названия городов. Реализуйте такую программу и для каждого из трёх городов укажите, в какой стране он находится. Если такого города нет, то выведите соответствующее сообщение.
# country1 = {}

# country = int(input('Vedite kolichestvo strany'))
# for c in range(country):
#     user = input('vedite stranu:').split()
#     country1[user[0]] = user[1:]
    
# for key,value in country1.items():
#     city = input('Enter a city: ')
#     if city in value:
#         print(f'Город {city} расположен {key}')
#     else:
#         print(f'По городу {city} данных нет.')
# print(country1)
# Пример: 

# Кол-во стран: 2

# 1 страна: Кыргызстан Бишкек Кант Каракол

# 2 страна: Германия Берлин Лейпциг Мюнхен

 

# 1 город: Москва

# Город Москва расположен в стране Россия.

 

# 2 город: Мюнхен

# Город Мюнхен расположен в стране Германия.

 

# 3 город: Рим

# По городу Рим данных нет.
