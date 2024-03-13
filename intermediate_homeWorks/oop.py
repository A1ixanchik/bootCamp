"""
1. Создайте класс BankAccount, в конструкторе которого определена переменная
экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
который будет отнимать сумму от баланса и возвращать текущий баланс. Также
добавьте метод deposit, который также имеет параметр amount и соответсвенно
добавляет сумму к балансу, возвращает баланс.
"""

# class BankAccount:
#     def __init__(self, balance) -> None:
#         self.balance = balance

        
#     def withdraw(self, amount):
#         self.balance -= amount
        

#     def deposit(self, amount):
#         self.balance += amount
        


# user1 = BankAccount(5600)

# user1.withdraw(100)
# user1.deposit(20)
# print(f'На вашем счете осталось {user1.balance}')   

"""
2. Вам дан такой код:

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
# class Nobel:
#     def __init__(self, category, year,winner ) -> None:
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         return f' Выиграл {2024 - self.year} лет назад'
        


# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())
"""
3. Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:
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
# class Password:
#     def __init__(self, password) -> None:
#         self.password = password


#     def validate(self):
#         if len(self.password) < 8 and len(self.password) > 15:
#             raise ValueError('You password has to contain more than 8 symbols but not more then 15')
#         elif len([x for x in self.password if x.isalpha()]) == 0:
#             raise ValueError('you password not given uppercase')
#         elif len([x for x in self.password if x.islower()]) == 0:
#             raise ValueError('you password not given lowercase')
#         elif len([x for x in self.password if x.isdigit()]) == 0:
#             raise ValueError('you password not given digit')
#         elif len([x for x in self.password if x in '!@#$%^&*()_-+=<>?/']) == 0:
#             raise ValueError('you password not given symbols')
#         else:
#             print('You passoword is saved succesessfully')

#     def __str__(self) -> str:
#         return '*' * len(self.password)
        

        

# pas1 = Password('1234fjdka;@')
# pas1.validate()    
# print(pas1)
  

        


"""
4. Создайте класс Math, экземпляром которого должно быть число.
У классa Math должно быть 3 метода:
- get_factorial - выводит факториал числа
- get_sum - выводит сумму цифр числа
- get_mul_table - выводит таблицу умножения для числа до 10. Создайте экземпляр класса и примените к нему все методы. 
"""
# class Math:
#     def __init__(self, digit) -> None:
#         self.digit = digit

#     def get_factorial(self):
#         res = range(1, self.digit)
#         count = 1
#         for i in res:
#             count *= i
#         return f'Факториал числа {self.digit}, равняется к {count}'
    
#     def get_sum(self):
#         count = 0
#         for i in str(self.digit):
#             count += int(i)
#         return f'Сумма числа {self.digit} равняется к {count}'

#     def get_mul_table(self):
#         number = self.digit

#         print(f"Таблица умножения для числа {number}:")

#         for i in range(1, number):
#             result = number * i
#             print(f"{i} x {number} = {result}")
        


# num1 = Math(11)
# print(num1.get_factorial())
# print(num1.get_sum())
# num1.get_mul_table()

"""
5. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д)

У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) с ключом в виде числа, 
приоритет который вы даете вашей задаче -
к примеру {3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
по приоритету:
[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]

"""
class ToDo:
    writer = {}
    def __init__(self, daily_planer) -> None:
        self.d_planner = daily_planer

    
    def give_priority(self, priority):
        self.writer[priority] = self.d_planner


    def list_of_tasks(self):
        # res = list(map(tuple,sorted(self.writer)))
        res = sorted(self.writer.items(), key=lambda x: x[0])
        print(res)

pr1 = ToDo('read book')
pr1.give_priority(3)
pr2 = ToDo('Learn to code',)
pr2.give_priority(1)
pr3 = ToDo('go to a gym',)
pr3.give_priority(2)


print(pr1.writer)
print(pr2.writer)
print(pr3.writer)

pr1.list_of_tasks()


            




        