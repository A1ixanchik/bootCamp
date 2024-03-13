# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .
# class Car:
#     def __init__(self, brand, year, color, horsepower=85):
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.h_power = horsepower

#     def get_auto(self):
#         print(f'Это машина {self.brand}, {self.year} года цвет машины {self.color}')

#     def add_horsepower(self):
#         if self.brand == 'Mers':
#             self.h_power += 40
#         elif self.brand == 'Bmw':
#             self.h_power += 40
#         elif self.brand == 'Porshe':
#             self.h_power += 40
#         else:
#             self.h_power += 20
#         print(f'Это машина {self.brand},лошадиных сил {self.h_power}')

#     def get_age_of_car(self):
#         print(f'Вашему {self.brand} машине {2024 - self.year} лет')

# car = Car('Bmw', 1999, 'Blue')
# car.get_auto()
# car.add_horsepower()
# car.get_age_of_car()

# car2 = Car('Subaru', 2004, 'Green')
# car2.get_auto()
# car2.add_horsepower()
# car2.get_age_of_car()

# Добавьте атрибут horsepower, который равен 85.

# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto

# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента.
# class Student:
#     def __init__(self, name, age, course) -> None:
#         self.name = name 
#         self.age = age
#         self.course = course

#     def get_student(self):
#         print(f'Это студент(ка) {self.name}, ему(ей) {self.age}лет он(она) учится в {self.course} курсе')

#     def get_birth_year(self):
#         print(f'Дата рождения {self.name} {2024 - self.age}')

# std = Student('Aiday', 20, 3)
# std.get_student()
# std.get_birth_year()
# std2 = Student('Ali', 20, 2)
# std2.get_student()
# std2.get_birth_year()