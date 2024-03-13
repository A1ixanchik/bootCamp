# class Dog:
#     # атрибуты
#     age = 0
#     ears = True

#     def __init__(self, name:str, color:str):
#         #self - это ссылка на объект который создается
#         self.at = name 
#         self.color = color

#     def bark(self):
#         print(f'{self.at} лает!')

#     def show_info(self):
#         print(f'Name: {self.at}, Age: {self.age}, color: {self.color}, ears: {self.ears}')
# rex = Dog('Rex', 'black')
# plout = Dog(name='Pluto', color='brown ')
# aktosh = Dog('Aktosh', 'gray')
# print(rex.at)

# rex.show_info( 
# )
# plout.show_info()
# aktosh.show_info()

# # rex.age = 2
# # plout.age = 7
# # aktosh.age = 1
# # aktosh.ears = False


# # rex.bark()
# # plout.bark()
# # aktosh.bark()


# class Human:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.golod = 100


#     def walk(self):
#             print(f'{self.name} walking around!')
#             self.golod += 30


#     def work(self):
#         print(f'{self.name} rabotu rabotaet!')
#         self.golod += 50

#     def eat(self, meal, finish=True):
#         print(f'{self.name} покушала {meal}!')
#         self.golod -= 60 if finish else 30
    

#     def info(self):
#          print(f'{self.name} --> {self.golod}')


# obj = Human('Raychel')
# obj.info()
# obj.eat('Kruasan ')
# obj.eat('Sandwich', finish=False)
# obj.info()


# Создайте класс Soda принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
# class Soda:
#     def __init__(self, suplements):
#         self.suplement = suplements

#     def show_my_drink(self):
#         if self.suplement == None:
#             print(f'Обычная газировка!')
#         else:
#             print(f'Газировка и {self.suplement}!')


# sup = Soda('limonad')
# sup.show_my_drink()

# Создайте класс Student. При создании его экземпляра, мы должны записать имя и фамилию студента в соответствующие переменные объекта. В классе должны быть:
#  1 переменная объекта books = [ ]
#  2 переменная объекта “knowledge” со значением по умолчанию 0
#  3 метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
#  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
#  5 Создайте экземпляры, вызовите методы.
# class Student:
   
 
#     def __init__(self, name, surname,):
#         self.name = name
#         self.surname = surname
#         self.books = []
#         self.knowledge = 0
        
  
#     def read_book(self, name_of_book):
#         self.name
#         self.books.append(name_of_book)
#         self.knowledge += 100
#         print(name_of_book)
    
#     def do_homework(self):
#         self.knowledge += 10 


    

# student1 = Student('Alihan', 'Kurmanbekov')
# student1.read_book('rich dad and poor dad')
# student1.do_homework()
# student2 = Student('anvar', 'King')
# student2.read_book('nothing matters')
# student2.do_homework()
# print(student1.books, student1.knowledge)
# print(student2.books, student2.knowledge)


# 6. Создайте класс имеющий атрибут "дата рождения" и автоматически просчитываемый возраст по входящей дате рождения. Используйте модуль time/datetime\
# import datetime
# class Birthday:
#     def __init__(self, day_of_birthday) -> None:
#         self.d_birthday = datetime.datetime.strptime(day_of_birthday, )
        
#     def age(self):
#         now_time = datetime.datetime.now()
#         print(now_time)
#         res = now_time - self.d_birthday
#         print(res)





# users_birthday = Birthday(2003-01-11)
# print(users_birthday.age())





# class Student:
#     def __init__(self, name, age, grade) -> None:
#         self.name = name 
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade
    

# class Course:
#     def __init__(self, name, max_students) -> None:
#         self.name = name 
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False 
    
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()

#         return value / len(self.students)


# st1 = Student('Tim', 19, 95)
# st2 = Student('Bill', 19, 75)
# st3 = Student('Jill', 19, 65)


# course = Course('Science', 2)

# course.add_student(st1)
# course.add_student(st2)

# print(course.get_average_grade())
class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    

    def show(self):
        print(f'I\'m a {self.name}, and i\'m {self.age} years old,')

class Cat(Pet):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    def speak(self):
        print('Meow')


class Dog(Pet):
    def speak(self):
        print('Gav Gav')


p1 = Pet('Rembo', 5)
p1.show()


c1 = Cat('Tom', 9)
c1.show()
c1.speak()


p1 = Pet('Rembo')
p1.show()