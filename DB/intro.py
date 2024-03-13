

# ORDER BY: Позволяет нам сортировать выводящие данные по убыванию или возрастанию. ASC(по возрастанию) и DESС(по убыванию)

# Синтаксис: SELECT <row> FROM <tablename>  ORDER BY <row> [ASC/DESC]


# WHERE: используется для фильтрации по полям. Будут выводится те данные которые соответсвуют условию оператора WHERE
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо'

# BETWEEN: условие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8 

# AND оператор и, для множественных условий 
# IN: WHERE <row> in (1, 2, 3, 4);
# LIMIT: ставит ограничение в кол-во получаемых данных

# LIKE: Выводит результат который соответсвует введенному шаблону для строк. Чувствителен к регистру 
# ILIKE: тоже самое только не зависит от регистра
# # Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чему либо'
# GROUP BY: разделяет данные которые мы получаем в SELECT, при этом группируя их по опрделенному признаку. И теперь для каждой группы можно использовать функцию 
# # HAVING: ставит условие при помощи которого данные отбираются в группировка

# Экспорт бд(дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# импорт: 
# -U <psqlusername> -d <dbname> -f <filename>



# Агрегатные функции: AVG(), COUNT(), MIN(), MAX(), SUM()


# --------------
# Ограничение:
    # 1. NOT NULL - обязательно к заполнению
    # 2. UNIQUE - уникальные данные
    # 3. CHECK -> CHECK age > - 1 - Ограничение проверки на условие 
    # 4. PRIMARY KEY(для установки идентификатора данных в таблице)
    # 5 FOREIGN KEY(для установки связей между таблицами)
    # 6. ON DELETE - для установки поведение при удалении данных которые были связаны


# ----------------------

# JOIN - выборка данных из двух таблиц, соединение таблиц 

# LEFT JOIN: выборка будет содержать все строки из левой таблицы
# RIGHT JOIN: выборка будет содержать все строки из правой 
#  таблицы

# SELECT P1.title, p1.price, o1.quantity, p1.price * o1.
# quantity as total_sum FROM products p1, orders o1 WHERE P1.ID = o1.product_id
# - Запрос сразу в две таблицы 


# SELECT P1.title, p1.price, o1.quantity, p1.price * o1.
# quantity as total_sum FROM products p1, orders o1 ON P1.ID = o1.product_id

# _----------------------_/
# Команда для добавления данных в таблицу 
# INSERT INTО <tablename> [(columns)] VALUES (data), (data)


# Команда для обновления данных:
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>

 
# Команда для удаления данных:
# DELETE FROM <table> WHERE <column> = <value>;

# --------------------------




 