"""
1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# class Circle:
#     circle_color = 'blue'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
        

#     def rashet(self):
#         mult = self.pi * self.radius**2
#         print(f'Ваш площадь равен круга  {mult}')


# res = Circle(12)
# res.circle_color = 'red'
# res.rashet()

"""
2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""

# class Song:
#     def __init__(self,s_author, s_title, s_year):
#         self.author = s_author
#         self.title = s_title
#         self.year = s_year
#     def show_author(self):
#         print(f'Это песня написана этим человеком {self.author}')

#     def show_title(self):
#         print(f'Заголовок этой песни: {self.title}')

#     def show_year(self):
#         print(f'Это песня была выпущена {self.year}')


# res = Song('Mirbek Atabekov', 'Kundor Janyrat', 2004)
# res.show_author()
# res.show_title()
# res.show_year()

    


        
# писать код здесь
"""
3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""
# class Taxi:
#     def __init__(self, name_of_company, total_cost,cost_for_km):

#         self.name_of_company = name_of_company
#         self.total_cost = total_cost
#         self.cost_for_km = cost_for_km

#     def counter(self):
#         counter_km = self.cost_for_km * 30
#         print(f'Спасибо что выбрали {self.name_of_company}, cтоимость за посадку {self.total_cost} сом  и стоимость за пройденные километры {counter_km}')


# namba_taxi = Taxi('Namba',50, 5)
# namba_taxi.counter()



        
# писать код здесь
"""
4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""

# class Telephone: 
#     def __init__(self,surname, number: int):
#         self.surname = surname
#         self.number = number

#     def get_info(self):
#         print(f'Контакт: {self.surname}, телефон:{self.number}')


# user = Telephone('Baktybkov Zhanybek',996708866493)
# user.get_info()
# писать код здесь
"""
5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""
# class Salary:
#     percentage = 8
#     def __init__(self,sum_of_salary: int, experience_job: int ):
#         self.experience = experience_job
#         self.salary = sum_of_salary
    
#     def counter_of_account(self):
#         print(f'Ваша опщая сумма налога:{self.salary * 8 // 100 * self.experience }')
    
    

# accounter = Salary(200_000, 4)
# accounter.counter_of_account()
        
# писать код здесь
    




# Создайте класс Soda принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».





# Создайте класс Student. При создании его экземпляра, мы должны записать имя и фамилию студента в соответствующие переменные объекта. В классе должны быть:
#  1 переменная объекта books = [ ]
#  2 переменная объекта “knowledge” со значением по умолчанию 0
#  3 метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
#  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
#  5 Создайте экземпляры, вызовите методы.   

        