# Дана база данных произведений Шекспира, в которой содержатся следующие таблицы: character - герои произведений, work - произведения, chapter главы произведений,

 

# paragraph - параграфы, wordform слова, встречающиеся в произведениях

 

# Напишите следующие запросы:

 

# 1. Найдите 10 самых часто встречающихся слов.

#  SELECT wordform, COUNT(*) as count
# FROM wordform
# GROUP BY wordform     
# ORDER BY count DESC
# LIMIT 10;
            


 

# 2. Найдите все слова, которые начинаются с буквы 'а', регистр не должен иметь значения.

# SELECT * FROM wordform WHERE plaintext ILIKE '%A%';
 

# 3. Найдите все произведения, которые относятся к жанру 'p'.


 

# 4. Найдите среднее количество параграфов в произведения жанра 'т'.

 

# 5. Выведите все произведения, в которых количество слов выше среднего.

 

# 6. Выведите имя героя, количество его реплик, и произведение, в котором этот герой встречается.

 

# 7. Выведите среднее количество реплик героев в произведении 'Romeo and Juliet'.

 

# 8. Выведите общее количество слов в каждой из секций в таблице paragraph.

 

# 9. Выведите всех героев, которые имеют от 15 до 30 реплик.

 

# 10. Выведите все произведения, которые были написаны в 17 веке

 

# 11. Найдите все произведения, которые имею в полном названии слово 'the'

 

# 12. Выведите все уникальные секции в paragraph.

 

# 13. Для каждой главы выведите: id, описание и название произведения, к которой относится данная глава.

 

# 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя

 

# 15. Для каждого параграфа выведите: номер параграфа, название произведения и год выхода этого произведения.