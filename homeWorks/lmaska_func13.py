# 1) Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра.
# user = int(input('enter a word: '))
# def counter_of_words(text):
#     counterA = 0
#     counterB = 0 
#     for x in text:
#         if x.islower():
#             counterB += 1
#         elif x.isupper():
#             counterA += 1
#     return f'lower: {counterB} upper: {counterA}'


# print(counter_of_words(user))


# 2) Напишите функцию, которая принимает число n и генерирует словарь, чьи ключи состоят из чисел от 1 до n, а их значения -- куб ключей. Пример: передано число 5. В результате должны получить словарь {1: 1, 2: 8, 3: 27, 4: 64}
# user = int(input('Введите число'))
# dict_ = {}
# def dict_generator(n):
#     for i in range(1, n):
#         dict_[i] = pow(i,3)
#     return dict_


# print(dict_generator(user))


        

# 3) Напишите функцию sum_range(start, end), которая суммирует все целые числа
#     от значения «start» до величины «end» включительно. Если пользователь задаст
#     первое число большее чем второе, просто поменяйте их местами.
# user1 = int(input('Enter a first number: '))
# user2 = int(input('Enter a second number: '))

# def sum_range(start, end):
#     res = 1
#     if start < end:
#         for i in range(start, end):
#             res += i
#     else:
#         for i in range(end, start):
#             res += i

#     return res


# print(sum_range(user1, user2))

