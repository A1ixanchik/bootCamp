# def sum_args(a, b, c=5, d=3):
#     return a + b + c + d


# result = print(sum_args(21, 34, 54, 34,))

# ==================================

# позиционные и именованные аргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(5, 10, 15)
# print()
# printParams(c=5, b=15, a=34)



# def sum_of_args(a, b, c, d):
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) #arguments(Позиционные аргументы)
# print(sum_of_args(a = 5, c=20, b=10, d=15)) #keyword arguments(Именованные аргументы)
# print(sum_of_args(5, 10, d=20, c=15))

# оператор *
# a = [1, 2, 3]
# b = [4, 5, 6]
# c1 = []
# for i in a and b:
#     c1.append(i)


# c = [*a, *b]
# print(c1)


# -----------------------------------------
# args , **kwargs

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# func(1, 2, 3, 4, 5, a = 1, b=5, c=3)
    

# def printScores(student, *scores):
#     print(f'Name of student: {student}')
#     print(f'Average: {sum(scores) / len(scores)}')
#     for x in scores:
#         print(f'Score: {x}')

# printScores('John Snow', 100, 90, 80, 95, 93)

# def printPetNames(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')

# printPetNames('John Snow', dog='Pluto', cat='Garfild', fish = ['Nemon', 'Dory', 'tima',], turtle = 'Leonardo')


# def get_some_data(a, b, *args, **kwargs):
#     print('Параметры а  и б:', a,b)
#     print('Параметры а  и б:', args)
#     print('Параметры а  и б:', kwargs)


# get_some_data(1, 2, 3, 4, 5, lang='Python', car='Subaru')

# ----------------------------
import string as s
# from random import choice , shuffle


# def generate_random_string(len_):
#     # print(s.ascii_letters, s.digits, s.punctuation)
#     symbols = s.ascii_letters + s.digits
#     res = [choice(symbols) for _ in range(1, len_)] + [choice(s.punctuation)]
#     shuffle(res)
#     return ''.join(res)
 
   
# print(generate_random_string(15))
# print(generate_random_string(10))
# print(generate_random_string(34))
# print(generate_random_string(88))



