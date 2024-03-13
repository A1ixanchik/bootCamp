# найти квадрат, куб, рузультат деления на 100 3 чисел
# num = 5
# {'num': 5, '2': 25, '3': 125, '100': 0.05}
# num1 = 5
# num2 = 75
# num3 = 1154
# res  = {'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1 / 100}
# res2  = {'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 / 100}
# res3  = {'num': num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3 / 100}

# print(res, res2, res3, sep='\n\n')
# DRY = don't repeat yourself


# def do_operations(num: int)-> None:
#     res = res  = {'num': num, '2': num ** 2, '3': num ** 3, '100': num / 100}

# do_operations(5)
# do_operations(75)
# do_operations(1154)

# _------------------------_
# Функция - это именованная часть программы, которая содержит в себе определенный блок кода, и может вызываться в других частях программы столько угодно
# def name_of_func(<a, b> параметры функции):
#     <body> код, какая то логика которая будет давать конечный результат 
#     <return> оператор который помогает сохранить результат


# параметры функции - переменные в которых мы временно сохроняем данные которые передаем при вызове в функцию ,
# они доступны только внутри функции

# аргументы - данные  которые мы передаем при вызове функции, они попадает в параметры по очередноо 

# def isEven(num):
#     return True if num % 2 == 0 else False


# res = isEven(16)
# res2 = isEven(17)
# print(res, res2)

# def isEven(num:int)-> bool:
#     """Return  True or False after checking number for even!"""
#     return True if num % 2 == 0 else False


# def sum_of_args(a:int, b: int, c: int = 0) -> int:
#     """returns sum of given arguments"""
#     try:
#         return a + b + c 
#     except TypeError:
#         raise Exception('Invalid values for arguments')


# print(sum_of_args(1, 2, 3))
# print(sum_of_args(16, 234, 34))
# print(sum_of_args(12, 21, None))



# print(len('String'))
# from typing import Iterable

# def our_len(obj: Iterable) -> None:
#     """Возврощяет длину итерируемого обьекта"""
#     i = 0
#     print(obj)
#     for _ in obj:
#         i += 1
    

#     print(f'result: {i}') 


# our_len([1, 2, 3, 4, 5])
# our_len('string Hello my name is John Snow')



def reverse_text(text: str)-> str:
    '''Reversing text!'''
    spisok = text.split()
    return ' '.join(spisok[:: -1])

str1 = 'Hello world my name is John, last name is Snow.Nice to meet you!!'

print(reverse_text(str1))
print(reverse_text('Hello world snow king!'))





