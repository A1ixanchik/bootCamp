# class Student:
#     univer = 'MIT'
#     def __init__(self, name) -> None:
#         self.name = name
#         self.books = []
#         self.language = {}
#         self.knowledge = 0
#         self.is_ready_work = False

#     def add_points(self, point):
#         self.knowledge += point
#         if self.knowledge > 500 and not self.knowledge.is_ready_work:
#             self.is_ready_work = True
#             print(f'{self.name}, get 500 points and ready to work!')
        


#     def read_book(self, book_name):
#         self.add_points(50)
#         self.books.append(book_name)

#     def do_project(self):
#         self.add_points(100)

#     def learn_lang(self, language, percent):
#         if percent not in range(70, 101):
#             print('Invalid points for lang')
#         else:
#             self.language[language] = percent
#             self.add_points(percent)



# st1 = Student(
#     'John Snow'
# )
# st2 = Student(
#     'Din Winchester'
# )
# print(f'Before study {st1.name}: {st1.books}, {st1.language}, {st1.is_ready_work}')
# print(f'Before study {st2.name}: {st2.books}, {st2.language}, {st2.is_ready_work}')


# st1.read_book('Grokam alghorithmy')
# st1.read_book('Python from beginer to Advanced')
# st1.read_book('Algorithms and data Structure')
# st1.read_book(
# 'Martin Ede '
# )
# st1.learn_lang('Python', 50)
# st1.learn_lang('Python', 90)
# st1.learn_lang('Js', 90)
# print(f'After study:{st1.name}: {st1.books}, {st1.language}, {st1.is_ready_work}')
# print(f"Ready to work:{st1.is_ready_work}")





# -----------------------------------------


# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model


#     def show_info(self):
#         return f'{self.brand} --> {self.model}'
    
#     def __str__(self) -> str:
#         return f'{self.brand} -> {self.model}'


# obj = Car('Bmw', '8 series')
# print(obj )
# print(obj.show_info())
        




# class Soda:
#     def __init__(self, suplement=None) -> None:
#         if isinstance(suplement, str):
#             self.suplement - suplement
#         else:
#             self.suplement = None
        
#     def __str__(self) -> str:
#         return 'Normal one!' if not self.suplement else f'Soda from {self.suplement}'


# a = Soda(1234)
# b = Soda(True)
# print(a, b )

# dushes = Soda('Grusha')
# limonad = Soda('Malina')
# print(dushes, limonad)


# =-------------------=
import random 

class Sniper:
    health = 100
    def __init__(self, name) -> None:
        self.name = name


    def __str__(self) -> str:
        return self.name
    

    def shoot(self, other):
        other.health -= 20
        print(f'Shooted {self}')
        print(f'У {other}, осталось {other.health}')





sniper = Sniper('John Snow')
sniper2 = Sniper('Din Winchester')


while sniper.health and sniper2.health:
    choice = random.randint(1,2)
    sniper.shoot(sniper2)if choice == 1 else sniper2.shoot(sniper)
    print()



print(f'{sniper if sniper.health else sniper2} won the game!')
    




        