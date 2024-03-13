# области видимости и пространство имен(scopes)
# Специяльная технология которая определяет контекст имени, в рамках которого мы можем ее использовать
# a = 5
# len()
# def func():
#     b = 10
#     print(b)
#     print(a)
# func()
# print(b)

# built-ins(встроенная область видимости) - print(), len()
# global(глобальная) - область одного файла
# <enclosed> (замкнутая (не локальная , nonlocal))
# local (локальная)-> область внутри одной функции

a = 20 #global
print #built

def hello():
    a = 'Hello' #local
    print(a, 'local', 'inside in func!')

hello()
print(a, 'global') 

# LEGB - local enclosed global built-in
                    #   ------------------------>>>>>>>>>>>>>>>>>>>>>>>>


# ______________--------------------______________
# замкнутая пространство имен  - локальное пространство у которого есть внутренное (вложенное) локальное пространство

# x = 'Global: '
# print(x, '1')# global


# def enclosed(): # global
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x, '3')
#     print(x, '2') # enclosed
#     local()
#     print(x,'4') # enclosed

# var = 0
# def increment():
    


# enclosed()
# print(x, "5")


# global - Позволяет изменять значение не локальной(замкнутой) переменной находясь внутри локальной области

# nonlocal -

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num +=1
#     return increment

# c_steps = counter()
# c_jumps = counter()
# print(c_steps)
# for _ in range(1, 1000):
#     c_steps()
    
# print(c_steps(), 'steps')




