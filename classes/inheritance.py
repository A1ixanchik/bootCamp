# Принципы ООП:
# 1. Наследование 
# 2. Инкапсуляция
# 3. Полиморфизм
# 4. Абстракция
# 5. Композиции
# 6. Агрегация

# __________------------------_________

# Наследование 
# Позволяет принимать родительские методы и атрибуты дочернему классу 
 
# Родительский класс
# Дочерный класс

class Animal:
    def print_info(self):
        print('I\'m an Animal!')



# class Lion(Animal):
#     pass


# class Dog(Animal):
#     pass


# simba = Lion()
# simba.print_info()
# rembo = Dog()
        

class Animal():
    def say(self):
        print(f'This animals name is {self.name}: {self.golos}')

    def eat(self):
        print(f'{self.name}, eats: {self.meal}')



# class Lion(Animal):
#     name = 'Simba'
#     golos = 'Growl'
#     meal = 'Meat'
#     griva = True

#     def info(self):
#         print(f'{self.name}, griva: {self.griva}')

# class Dog(Animal):
#     name = 'Rembo'
#     golos = 'bark'
#     meal = 'Meat'


# class Koala(Animal):
#     name = 'Koala'
#     golos = 'Growl'
#     meal = 'grass'


# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()
# print()

# simba.say()
# simba.eat()
# simba.info()
# print()

# julian.say()
# julian.eat()
# print()
        

# class Person:
#     def infor(self):
#         print('I\'m person from Bishkek!')


# class Student(Person):
#     def info(self):
#         print('I\'m study at Manas University')

# obj = Student()
# obj.info()
        
# class Laptop:
#     def __init__(self, brand, model, price) -> None:
#         self.brand = brand
#         self.model = model
#         self.price = price



#     def get_info(self):
#         return{'brand': self.brand, 'model': self.model, 'price': self.price}
    




# class Acer(Laptop):
#     def __init__(self, model, price, year, videocard) -> None:
#         super().__init__('Acer', model, price)
#         self.year = year
#         self.videocard = videocard

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['vidoecard'] = self.videocard


# class Apple(Laptop):
#     def __init__(self, model, price, year, display) -> None:
#         super().__init__('MacBook', model, price)
#         self.year = year
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['display'] = self.display


# mac = Apple('Pro', 1500, 14, 2020)
# print(mac.get_info())

# acer = Acer('swift', 600, 2019, 'Nvidia')
# print(acer.get_info())




