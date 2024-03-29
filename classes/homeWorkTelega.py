# Задача: Создание системы учета сотрудников для компании

# Цель: Разработать классы для управления информацией о сотрудниках в компании, включая их отделы, должности и личные данные.

# Описание:

# Класс Employee:

# Атрибуты: name (имя сотрудника), employee_id (ID сотрудника), position (должность), department (отдел).
# Методы:
# Конструктор для инициализации атрибутов.
# promote(new_position) - повышение сотрудника на новую должность.
# transfer(new_department) - перевод сотрудника в другой отдел.
# __str__() - возвращает информацию о сотруднике.
# Класс Department:

# Атрибуты: name (название отдела), department_id (ID отдела), employees (список сотрудников в отделе).
# Методы:
# Конструктор для инициализации атрибутов.
# add_employee(employee) - добавляет сотрудника в отдел.
# remove_employee(employee_id) - удаляет сотрудника из отдела.
# get_employees() - возвращает список сотрудников отдела.
# __str__() - возвращает информацию об отделе и его сотрудниках.
# Класс Company:

# Атрибуты: name (название компании), departments (список отделов в компании), employees (список всех сотрудников).
# Методы:
# Конструктор для инициализации атрибутов.
# add_department(department) - добавляет новый отдел в компанию.
# add_employee(employee, department_id) - регистрирует нового сотрудника и добавляет его в указанный отдел.
# find_employee(employee_id) - ищет сотрудника по ID.
# find_department(department_id) - ищет отдел по ID.
# transfer_employee(employee_id, new_department_id) - переводит сотрудника в другой отдел.
# Задание:
# Реализуйте вышеуказанные классы с соответствующими атрибутами и методами. Создайте взаимодействие между классами так, чтобы можно было управлять информацией о сотрудниках, их должностях и отделах. Обеспечьте возможность добавления новых сотрудников и отделов, а также перевода сотрудников между отделами и их повышения в должности.
