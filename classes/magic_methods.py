# magic methods (магические методы)
# dunder methods(double underscore) -> __init__
# служебные методы

# Магия (фишка) заключается в том что эти методы запускаются в том эти методы запускаются без прямого обращения к ним, определение методы могут отвечать за определение операторы
# Магические методы сравнения
# __eq__(self, other) -> 5 == 8

# __ne__ -> !=
# __lt__ -> < 
# __gt__ -> >
# __le__ -> <= 


# print('15'< 'ABC')
# class Word(str):
#     def __new__(cls, obj):
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)

#     def __init__(self, obj) -> None:
#         super().__init__()
#         self.obj = obj

#     def __gt__(self, other):
#         print('gt worked')
#         print(self, '=====', other)
#         if len(self) > len(other):
#             return self
#         elif len(self) < len(other):
#             return other
#         else:
#             return 'eq'
        
#     def __lt__(self,other) -> bool:
#         return len(self) < len(other)
    
     
#     def __eq__(self, other) -> bool:
#         return len(self) == len(other)



# obj = Word('           Hello John        ')
# obj2 = Word('Co di fy')

# print(obj > obj2)
# print(obj < obj2)
# print(obj == obj2)

# + - / * // % **


# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __div__(py2) , -> __truediv__(py3)
# % -> __mod__
# # ** -> __pow__


# class Digit():
#     def __new__(cls, *args, **kwargs):
#         print(cls, '!!!!!!!')
#         # print(*args)
#         # print(**kwargs)
#         number = abs(args[0])
#         # print(number)
#         instance = super().__new__(cls)
#         # print(instance)
#         instance.number = number
#         return instance
    
#     def __add__(self, other):
#         print('add worked!')
#         res  = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')
#         return res
    
# number = Digit(12)
# number2 = Digit(123)
# print(number + number2)


# _____________--------------________________
# from random import choice

# class Dog:
#     def sound(self):
#         print('Bark!')
    

# class Cat:
#     def sound(self):
#         print('Meow Meow!')


# class Horse:
#     def sound(self):
#         print('Igo-igo-igo')


# class Pet:
#     def __new__(cls):
#         pet = choice([Dog, Cat, Horse])
#         self = super().__new__(pet)
#         print(f'I\'m {type(self).__name__}')
#         return self


#     def __init__(self) -> None:
#         print('Pet never was called!')


# pet = Pet()
# pet.sound()



# --------------------------
# SINGLETON
# class Singleton:
#     _instance = None



#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super(). __new__(cls)
#         return cls._instance
    

#     def __str__(self) -> str:
#         return str(id(self))


# a = Singleton()
# v = Singleton( )
# print(a, v)
# print(a is v)
        


# ______--------_____________
class Kopilka:
    def __init__(self) -> None:
        self.total = 0
        self.coins = []

    def add_coin(self, coin):
        self.total += coin
        self.coins.append(coin)

    def __len__(self):
        return len(self.coins)

    def __getitem__(self, index):
        return self.coins[index - 1]

from itertools import repeat
from random  import choice, randint


obj = Kopilka()
for f in repeat(choice, randint(89, 156)):
    obj.add_coin(f([1, 3, 5, 10, 4]))


obj.add_coin(10)
obj.add_coin(1)
obj.add_coin(4)
print(obj.coins)
print(obj.total)
print(len(obj))
print(obj[1])
print(obj[2])
print(obj[3])
for x in obj:
    print(x)