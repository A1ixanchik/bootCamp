# Инкапсуляция конструкция, которая помогает связать данные с методами для их обработки и управления (связь между данными и методами которые упровляют ими)(класс - капсула)
# 2. Механизм сокрытия, при помощи которогоо можно ограничить доступ одного компонента программы к другому 


# инкапсуляция как свазь
# class Phone:
#     number = '+99999939798'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')
#         print(f'Мой номер: {Phone.number}')


# my_phone = Phone()
# my_phone.print_number()



# Инкапсуляция как механизм сокрытия 
# 3 уровня сокрытия данных в питоне
#    1. Публичный (public)  - number, print_number
#    2. Защищенный(_protected) - _number
#    3. Приватный(__private) - __number


# class Car:
#     _country = 'Kyrgyzstan'
#     __motor = 'GT'

    
#     def __init__(self) -> None:
#         self.marka = 'Bmw' #Public
#         self._model = 'I8' #Protected
#         self.__color = 'black' #private


# obj = Car()
# print(dir(obj))
# print(obj.marka)
# print(obj._country, obj._model)
# print(obj._Car__color, obj._Car__motor)


# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 17


#     def call(self):
#         print(f'{self._caller}, звонит вам!')
#         question = input('Взять трупку (yes/no): ')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Сбросили трубку!')


#     def __turn_on(self):
#         self.__increment_calls()
#         print('Alloo')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

#     def __increment_calls(self):
#         self.__count_of_calls += 1


# john = Phone()
# print(john.username)
# john.call()
# john.call()
# john.call()
# john.call()


# ----------------------------

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name 
#         self.age = age

#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old!')



# obj = Person('John', 18)
# obj.display_info()
# obj.name = [1, 2, 3, 4, 5]
# obj.age = -25
# obj.display_info()



# ==================================
# getter & setter 
# они нужны чтобы избежать прямого обращения к сокрытым атрибутам
# при этом можно добавить логику валидация(проверки) данных которые будут установленны в атрибут

# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name 
#         self.__age = age

#     def display_info(self):
#         print(f'My name is {self.__name} and I\'m {self.__age} years old!')

#     # getter
#     def name(self): return self.__name
    

#     def age(self): return self.__age


#     # setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Name  must be str object!')

#         else: 
#             self.__name = name
#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print('Invalid value for age!')

#         else: 
#             self.__age = age


# obj = Person('John', 24)
# obj.display_info()
# obj.set_name(55)
# obj.set_age(-12)
# obj.display_info()
# obj.set_name('Jamie')
# obj.set_age(26)
# obj.display_info()




    
# obj = Person('John', 18)
# obj.display_info()
# obj.name = [1, 2, 3, 4, 5]
# obj.age = -25
# obj.display_info()




class Item:
    def __init__(self, name) -> None:
        self.name = name 


obj = Item('alihan')
print(obj)