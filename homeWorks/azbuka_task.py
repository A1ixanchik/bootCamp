# 1 задача:

#  Напишите программу, которая  симулирует игру лото с одной картой. Начните с генерирования списка их всех возможных номеров выпадения (от В1 до О75). После этого перемешайте номера в хаотичном порядке, воспользовавщись функцией shuffle из модуля random. Вытаскивайте по одному номеру из списка и зачеркивайте номера, пока карточка не окажется выигравшей. Приведите 1000 симуляций и выведите на экран минимальное, максимальное и среднее количество извлечений номеров, требующееся для выигрыша.

from random import shuffle

res = []
for _ in range(1000):
    bilet = [['b7',  'b54', 'b64', 'b12', 'b13'],
             ['i5',  'i6',  'i8',  'i9',  'i10'],
             ['n11', 'n12', 'n13', 'n14', 'n15'],
             ['g16', 'g6',  'g29', 'g41', 'g54'],
             ['o16', 'o17', 'o36', 'o41', 'o54']]

    # мешок из которого достаем рандомный номер билета
    meshok = [x + str(i) for i in range(1, 76) for x in 'bingo']
    shuffle(meshok)

    # количество извлечений номеров
    draw = 0

    # Создаем два списка с диагоналями

    # bilet = [['b7',  'b54', 'b64', 'b12', 'b13'],
    #          ['i5',  'i6',  'i8',  'i9',  'i10'],
    #          ['n11', 'n12', 'n13', 'n14', 'n15'],
    #          ['g16', 'g6',  'g29', 'g41', 'g54'],
    #          ['o16', 'o17', 'o36', 'o41', 'o54']]
    diagonals = [[], []]
    i = 0
    i2 = -1
    for row in bilet:
        diagonals[0].append(row[i])
        diagonals[1].append(row[i2])
        i += 1
        i2 -= 1
    # print(diagonal)

    flag = True
    while flag:
        number = meshok.pop()
        draw += 1

        # Проверка выигрыша по горизонтали
        for row in bilet:
            if number in row:
                row[row.index(number)] = 'X'
                if all(cell == 'X' for cell in row):
                    flag = False

        # Проверка по вертикали
        for i in range(5):
            column = [row[i] for row in bilet]
            if all(cell == 'X' for cell in column):
                flag = False

        # Проверка по диагонали
        for diagonal in diagonals:
            if number in diagonal:
                diagonal[diagonal.index(number)] = 'X'
                if all(cell == 'X' for cell in diagonal):
                    flag = False
    res.append(draw)
    draw = 0
print(res)
print(f'Максимальное количество вытаскиваний номеров из мешка равно {max(res)}\nМинимальное количество вытаскиваний номеров из мешка равно {min(res)}')

2 задача:

    Азбука Морзе зашифровывает буквы и цифры при помощи точек и тире.
    В данном упражнении вам необходимо написать программу, в которой
    соответствие символов из азбуки Морзе будет храниться в виде словаря.
    В табл. 6.3 приведена та часть азбуки, которая вам понадобится при ре-
    шении этого задания.
    В основной программе вам необходимо запросить у пользователя стро-
    ку. После этого программа должна преобразовать его в соответствующую
    последовательность точек и тире, вставляя пробелы между отдельными120  Упражнения
    символами. Символы, не представленные в таблице, можно игнорировать.
    Например, сообщение Hello, World! может быть представлено следующей
    последовательностью: .... . .–.. .–.. ––– .–– ––– .–. .–.. –..
    Таблица 6.3. Азбука Морзе

    Символ     Код     Символ     Код     Символ     Код     Символ     Код
    A               .–        J                 .–––     S               ...        1               .––––
    B               –...      K                –.–       T               –           2              ..–––
    C               –.–.      L                .–..      U               ..–        3              ...––
    D               –..       M               ––         V              ...–        4              ….–
    E               .          N                –.         W             .––         5             …..
    F               ..–.      O                –––       X              –..–        6             –….
    G               ––.       P                .––.      Y              –.––        7             ––...
    H               ….       R                ––.–     Z              ––..         8            –––..
    I                ..         S                .–.        0              –––––      9            ––––.



morza = {'A': ' .- ', 'J': ' .--- ', 'S': ' ... ', '1': ' .---- ',
'B': ' -... ', 'K': ' -.- ', 'T': ' - ', '2': ' ..--- ',
'C': ' -.-. ', 'L': ' .-.. ', 'U': ' ..- ', '3': ' ...-- ',
'D': ' -.. ', 'M': ' -- ', 'V': ' ...- ', '4': ' ….- ',
'E': ' . ', 'N': ' -. ', 'W': ' .-- ', '5': ' ….. ',
'F': ' ..-. ', 'O': ' --- ', 'X': ' -..- ', '6': ' -…. ', 
'G': ' -. ', 'P': ' .--. ', 'Y': ' -.-- ', '7': ' --... ',
'H': ' …. ', 'R': ' --.- ', 'Z': ' --.. ', '8': ' ---.. ',
'I': ' .. ', 'S': ' .-. ', '0': ' ----- ', '9': ' ----. '}
user = input('enter a word: ').upper()
str1 = ''
for i in user:
    if i in morza:
        str1 += morza[i]
        
    
    
    

print(str1)
    
 
