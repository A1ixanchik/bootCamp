"""
1) В текстовом файле посчитать количество строк, а также для каждой
отдельной строки определить количество в ней символов и слов.
"""
# with open('file.txt', 'r') as file:
#     stroki = len(file.readlines())
#     file.seek(0)
#     for i in file.readlines():
#         print(f'Количество символов:{len(i.replace(' ', ''))}')
#         print(f'Количество слов в строке: {len(i.split())}')
     

# Писать код здесь

"""
2) Создайте файл nums.txt, содержащий несколько чисел, записанных через
пробел. Напишите программу, которая подсчитывает и выводит на экран
общую сумму чисел, хранящихся в этом файле.
"""

# with open ('file.txt', 'r') as file:
#     sums = 0
#     for i in file:
#         for x in i.split():
#             x = int(x)
#             sums += x
#     print(sums)

# Писать код здесь

"""
записать их произведение в файл output.txt.
3) Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем
"""
# with open('output.txt', 'w') as file:
#     result = 1
#     with open('input.txt', 'r') as read_file:
#         nums = read_file.readline().split()
#         for num in nums:
#             result = result * int(num)
#     file.write(str(result))




# Писать код здесь

"""
4) В файле записаны в целые числа. Найти максимальное и минимальное
число и записать в другой файл.
"""
# with open('output.txt', 'w')as file:
#     with open('input.txt', 'r') as max_int:
#         nums = list(map(int, max_int.readline().split()))
#         
#     file.write(str(max(nums))+ '\n')
#     file.write(str(min(nums)))

# Писать код здесь

"""
5) В файле записаны в столбик целые числа. Отсортировать их по
возрастанию суммы цифр и записать в другой файл.
"""
# Писать код здесь
# with open('output.txt', 'w') as file:
#     with open('input.txt', 'r') as sort:
#         res = [int(x.replace('\n', '')) for x in sort.readlines()]
#         res = sorted(res)
#     file.writelines([str(i) + '\n' for i in res])

    
# 6) Напишите функцию read_last(lines, file), которая будет открывать определенный файл. file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым: Вечерело Жужжали мухи Светил фонарик Кипела вода в чайнике Венера зажглась на небе Деревья шумели Тучи разошлись Листва зеленела
# def read_lines(line, file):
#     with open(file, 'r')as file:
#         result = file.readlines()
#         print(result[-line:])

# read_lines(2, 'article.txt')


# 7) Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной директории можно осуществить при помощи функции walk() модуля os.

# from os import walk

# def print_docs(folder:str):
#     for x in walk(folder):
#         print(x)


# print_docs('test')




# 8) Документ «article.txt» содержит следующий текст: Вечерело Жужжали мухи Светил фонарик Кипела вода в чайнике Венера зажглась на небе Деревья шумели Тучи разошлись Листва зеленела Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
# def longest_words():
#     with open('hwText/article.txt') as file:
#         long_word = file.readline()
#         words = long_word.split()
#         longest_word = max(words,key=len)
#         print(longest_word)

# longest_words()

# 9) Требуется создать csv-файл «rows_300.csv» со следующими столбцами: – № - номер по порядку (от 1 до 300); – Секунда – текущая секунда на вашем ПК; – Микросекунда – текущая миллисекунда на часах. На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
# import csv
# import time

# with open('rows_300.csv', 'w', newline='') as csvfile:   
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(['№', 'Секунда', 'Микросекунда'])  
#     for i in range(1, 301):      
#         current_time = time.time()
#         second = int(current_time)
#         microsecond = int((current_time - second) * 1000)      
#         csv_writer.writerow([i, second, microsecond])
#         time.sleep(0.01)

# print("Общая стоимость заказа:", total_order_cost, "руб.")

# 10) Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# наименование товара;
# количество товара (целое число);
# цена (в рублях) товара за 1 шт. (целое число).
# Напишите программу, подсчитывающую общую стоимость заказа.
# def calculate_total_order(file_name):
#     total_cost = 0
#     with open(file_name, 'r') as file:
#         for line in file:
#             parts = line.strip().split('\t')
#             item_name = parts[0]
#             quantity = int(parts[1])
#             price_per_unit = int(parts[2])
#             total_cost += quantity * price_per_unit
    
#     return total_cost
# file_name = 'prices.txt'
# total_order_cost = calculate_total_order(file_name)

# print("Общая стоимость заказа:", total_order_cost, "руб.")


# 11) Словарь из csv. Имеется файл data.csv, содержащий информацию в csv-формате. Напишите функцию read_csv() для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей. Функция read_csv() не должна принимать аргументов.
# def read_csv():
#     with open('cars_.csv', 'r') as file:
#         result = {}
#         first_line = file.readline()
#         first_line = first_line.split(',')
#         all_lines = file.readlines()

#         first = [x.split(',')[0] for x in all_lines]
#         second = [x.split(',')[1] for x in all_lines]
#         third = [x.split(',')[3] for x in all_lines]
#         four = [x.split(',')[4] for x in all_lines]
#         five = [x.split(',')[5] for x in all_lines]
#         result[first_line[0]] = first
#         result[first_line[1]] = second
#         result[first_line[2]] = third
#         result[first_line[3]] = four
#         result[first_line[4]] = five
#         print(result)
# read_csv()


# 12) Запрещенные слова
# Напишите программу, которая получает на вход строку с названием текстового файла, и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
# Формат ввода
# Строка текста с именем существующего текстового файла, в котором необходимо заменить запрещенные слова звездочками.
# Формат вывода
# Текст, отредактированный в соответствии с условием задачи.
# Пример ввода вывода
# Предположим, что forbidden_words.txt содержит следующие запрещенные слова:
# hello email python the exam wor is
# А текст файла, подлежащего цензуре, выглядит так:
# Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
# Тогда программа должна вывести отредактированный текст в таком виде:
# *, *ld! **  * programming language of * future. My * .... **  awesome!!!!
# dict_ = {'students': 'grades'}


# def censored(file=input("Введите имя файла с запрещенными словами: "), text = input("Введите имя текстового файла: ").lower()):
#     with open(file, 'r') as f:
#         forbidden_words = f.read().split()
#     for word in forbidden_words:
#         text = text.replace(word, '*' * len(word))
#     censored_text = ''
#     i = 0
#     for symbol in text:
#         if symbol.isalpha():
#             if text[i].isalpha():
#                 if text[i] == symbol.lower():
#                     censored_text += '*'
#                 else:
#                     censored_text += symbol
#                 i += 1
#             else:
#                 censored_text += symbol
#         else:
#             censored_text += symbol
#     return censored_text



# 13) В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов
# Открываем файл для чтения
# with open('students_info', 'r') as file:
#     grades = file.readlines()
#     result = []
#     for grade in grades:
#         student = grade.replace('\n', '')
#         if int(student[-1]) < 3:
#             result.append(student)
#     for student in result:
#         print(student)



# 14) Выведите в обратном порядке содержимое всего файла полностью. Для этого считайте файл целиком при помощи метода read().
# Примеры
# входные данные:
# Beautiful is better than ugly. 
# Explicit is better than implicit. 
# Simple is better than complex.
# Complex is better than complicated.

# выходные данные:
# .detacilpmoc naht retteb si xelpmoC 
# .xelpmoc naht retteb si elpmiS 
# .ticilpmi naht retteb si ticilpxE 
# .ylgu naht retteb si lufituaeB


# with open('text', 'w') as file:
#     file.write('Beautiful is better than ugly.\n')
#     file.write('Explicit is better than implicit.\n')
#     file.write('Simple is better than complex.\n')
#     file.write('Complex is better than complicated.\n')
#     print()

# with open('text', 'r') as file:
#     reading = file.read()[::-1]

#     print(str(reading))



        



            

        
        
    
    



