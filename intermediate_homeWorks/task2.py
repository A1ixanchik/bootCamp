"""

1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.

"""
# class Class1:
#     def add1(self, x):
#         print(x + 1)

#     def mult_by_one(self, x):
#         print(x * 1)


# class Class2(Class1):
#     def meow(self):
#         print('Meow')

#     def bark(self):
#         print('Gav Gav')


# ob1 = Class2()
# ob1.add1(9)
# ob1.mult_by_one(9)
# ob1.meow()
# ob1.bark()

# писать код здесь

"""

2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.

"""
# class A:
#     def method1(self):
#         return 'Основной функционал!'


# class B(A):
#     def method1(self):
#         repr = super().method1()
#         print(repr)
#         print("Дополнительный функционал!")
        
    
# ob1 = B()
# ob1.method1()


# писать код здесь

"""

3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:

append, который будет принимать строку и добавлять её в конец исходной

pop, который удаляет из строки последний элемент и возвращает его.

Пример:

# example = MyString('String')

# example.append('hello')

# print(example) -> 'Stringhello'

# print(example.pop()) -> 'o'

# print(example) -> 'Stringhell'

"""
# Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:

# append, который будет принимать строку и добавлять её в конец исходной

# pop, который удаляет из строки последний элемент и возвращает его.
# class MyString(str):
#     def __init__(self, first_str) -> None:
#         self.first_str = first_str
        
#     def append(self, string):
#         self.first_str = self.first_str + string
#         print(self.first_str)

    
#     def pop(self):
#         return self.first_str[-1]



# example = MyString('Hello')
# example.append('Method')
# print(example.pop())
        


# писать код здесь

"""

4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.

"""
# class MyDict(dict):
#     def __init__(self, dict1):
#         self.dict = dict1

#     def get(self, key):
#         if self.dict.get(key) == None:
#             return 'Are you kidding?'
#         else:
#             return self.dict.get(key)


    
# dict1 = MyDict({'1': 'asddasd', 2: 'asd'})
# print(dict1.get('1'))
# писать код здесь



"""

5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.

Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.

"""
# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f'Hello my name is {self.name}, and I\'m {self.age} years old!')



# class Student(Person):
#     def __init__(self, name, age, proffesion) -> None:
#         super().__init__(name, age)
#         self.proffesion = proffesion

#     def display_student(self):
#         print(f'Hello my name is {self.name}, I\'m {self.age} years old and my proffecincy is {self.proffesion}')


# st1 = Student('Alihan', 20, 'Sofware engineering')
# st1.display_student()


        

# писать код здесь

"""

6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.

"""
# class ContactList(list):
#     def __init__(self,ls):
#         self.list = ls
    
#     def search_by_name(self, name):
#         res = []
#         for i in self.list:
#             if name == i:
#                 res.append(i)
        
#         return res

            
# all_contacts = ContactList(['Alihan', 'Jasmin', 'Jake', 'Kurmanbek'])         
# print(all_contacts.search_by_name('Alihan'))
# print()
# писать код здесь
 

"""

7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию

должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

Создайте два дочерних класса от Smartphone - Iphone и Samsung.

У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.

А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.

Создайте объекты от данных классов и примените все методы.

"""
# from datetime import datetime

# class Smartphone:
#     def __init__(self,name, color, memory, battery = 0) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

        
#     def __str__(self) -> str:
#         return f'Телефон {self.name}, {self.memory}'
    
#     def charger(self, charge):
#         self.battery += charge
#         return f'Ваша зарядка заряжена на {self.battery}'
    
# class Iphone(Smartphone):
#     def __init__(self, name, color, memory, ios,battery=0,) -> None:
#         super().__init__(name, color, memory, battery)
#         self.ios = ios
        
#     def send_imessage(self):
#         return f'Это сообщение было отправлено вам от {self.ios}'
    


    
# class Samsung(Smartphone):
#     def __init__(self, name, color, memory, android,battery=0,) -> None:
#         super().__init__(name, color, memory, battery)
#         self.android = android

#     def show_time(self):
#         hours = datetime.now()
#         return f'Время на часах {hours}'
        
       

# obj = Iphone('Apple', 'blue', '16gb','MacBook air m1', 'Hello my name is iphone 14')
# print(obj.send_imessage())
# print(obj)

# obj1 = Samsung('Android', 'blue', '16gb','Samsung s8', 'Hello my name is iphone 14')
# print(obj1.show_time())
# print(obj1)
"""

8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.
 

У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.

 

Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:

 

Открытие замков: Alohomora

позволяет магу попасть в любую комнату,

способно открыть любую закрытую замочную скважину.

 

Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

"""
#  Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.
 

# У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.
# class Spell:
#     def __init__(self, name, formula) -> None:
#         self.name = name 
#         self.formula = formula

#     def get_description(self):
#         return f'заклинание левитации, которое заставляет парить в воздухе объекты.'
    
#     def execute(self, spell_word):
#         if spell_word == 'vingardium liviosa':
#             return f'Ваше заклинание сработала вы подняли орга и спасли Гарри Поттера'
        
#     def __str__(self) -> str:
#         return f'{self.name}\n {self.get_description}'
    

# magic = Spell('Levioso','vingardium liviosa')
# print(magic)
# print(magic.execute('vingardium liviosa'))
# print(magic.get_description())


"""

9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом

чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

Создайте исключение от этого класса с сообщением:

"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"

 

Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:

 

Traceback (most recent call last):

  File "inheritance.py", line 121, in <module>

    check_letters(a)

  File "inheritance.py", line 117, in check_letters

    raise capitals_error

main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

 

"""
# 9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом

# чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

# Создайте исключение от этого класса с сообщением:

# class CustomError(Exception):
#     def __init__(self, message) -> None:
#         self.message = message

#     def check_letter(self):
#         if any([i.islower() for i in self.message]):
#             raise CustomError('Только большие буквы разрешены!')
#         else:
#             return 'done'

    
# obj1 = CustomError('MOOOOOO')
# print(obj1.check_letter())
        


"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"
 

"""

10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:

power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

 

Класс должен иметь методы:

give_weapon - выбирает случайное оружие из списка

 

give_role - выбирает случайную роль из списка, к примеру:

["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

 

give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:

char1.give_powers('ловкость', 5)

увеличит ловкость вашего героя.

 

Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,

дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.

"""



# import random 
# class Character:
#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
#     character = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

#     weapons = ["Энергетический меч", "Электрошоковый дрон", "Лазерный бластер", "Плазменная винтовка", "Кинетический диспетчер", "Ионный гранатомет", "Сингулярный рейдер"]

#     def __init__(self, name) -> None:
#         self.name = name
#         self.weapon = None
#         self.role = None

#     def give_weapon(self):
#         self.weapon = random.choice(self.weapons)
#         return self.weapon
    
#     def give_role(self,):
#         self.role = random.choice(self.character)
#         return self.role
    
#     def give_powers(self,key, value):
#         self.power_list[key] = value
#         return self.power_list



# class Elf(Character):
#     def __init__(self, name, archery1) -> None:
#         super().__init__(name)
#         self.archery1 = archery1
#     def archery(self):
#         return 'Эльф попал в орга!'
    

# class Orc(Character):
#     def __init__(self, name, orc) -> None:
#         super().__init__(name)
#         self.orc = orc
#     def eat(self):
#         return 'Орг сьел эльфа!'
    

# class DragonBorn(Character):
#     def __init__(self, name, drago) -> None:
#         super().__init__(name)
#         self.drago = drago
#     def destroy(self):
#         return 'Драго уничтожил всех!'
    

# elf1 = Elf('Мелькор', 'strelat')
# print(elf1.give_powers('мудрость', 20))
# print(elf1.give_weapon())
# print(elf1.archery())


# orc1 = Orc('Мелькор', 'strelat')
# print(orc1.give_powers('харизма', 20))
# print(orc1.give_weapon())
# print(orc1.eat())

# drago = DragonBorn('Drago', 'strelat')
# print(drago.give_powers( 'мудрость', 20))
# print(drago.give_weapon())
# print(drago.destroy())

"""
1. Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. 
Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например:
"Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""
# class Song:
#     def __init__(self, author, title, release) -> None:
#         self.author = author
#         self.title  = title
#         self.release = release


#     def show_author(self):
#          return f'Это песня была написона певцом {self.author}'

    
#     def show_title(self):
#         return f'Это песня называется {self.title}'

    
#     def show_year(self):
#         return f'Это песня была выпущена в {self.release}'


# s1 = Song('Mirbek Atabekov', 'Kundor Janyrat', 2005)
# print(s1.show_author())
# print(s1.show_title())
# print(s1.show_year())
        


"""
3. Создайте класс BankAccount, в конструкторе которого определена переменная
экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
который будет отнимать сумму от баланса и возвращать текущий баланс. Также
добавьте метод deposit, который также имеет параметр amount и соответсвенно
добавляет сумму к балансу, возвращает баланс.
"""
class BankAccount:
    



"""
4. Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""




"""
5. Создайте класс телефонной книги. У контактов должны быть имена и фамилии и телефонные номера. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888". Затем объявите экземляр класса и вызовите метод.
"""

"""
7. Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда")
print(winner1.category, winner1.year, winner1.winner)
print(winner1.get_year())

winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
print(winner2.category, winner2.year, winner2.winner)
print(winner2.get_year())



который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 50 лет назад

Литература 1994 Кэндзабуро Оэ
выиграл 27 лет назад

Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале. Даты внутри класса не хардкодить.
"""



"""
8. Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:
- пароль должен быть минимум 8 символов, но меньше 15
- пароль должен содержать цифры
- пароль должен содержать буквы
- пароль должен содержать хотя бы один из символов:
    '@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите кастомное исключение, 
если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

Также переопределите метод str, чтобы при попытке распечатать
сам пароль, вам выдавалась строка из звездочек,
к примеру пароль - 'joe@123456'
в терминале выйдет - ******
"""


"""
9. Создайте класс Math, экземпляром которого должно быть число.
У классa Math должно быть 3 метода:
- get_factorial - выводит факториал числа
- get_sum - выводит сумму цифр числа
- get_mul_table - выводит таблицу умножения для числа до 10. Создайте экземпляр класса и примените к нему все методы. 
"""

"""
10. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д)

У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) с ключом в виде числа, 
приоритет который вы даете вашей задаче -
к примеру {3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
по приоритету:
[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]

"""
    

        


        
