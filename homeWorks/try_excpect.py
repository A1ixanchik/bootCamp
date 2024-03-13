# Пользователь хочет установить пароль для своей учетной записи. Пароль должен соответствовать следующим критериям:

# Длина пароля должна быть не менее 8 символов.
# Пароль должен содержать хотя бы одну заглавную букву (A-Z).
# Пароль должен содержать хотя бы одну строчную букву (a-z).
# Пароль должен содержать хотя бы одну цифру (0-9).
# Пароль должен содержать хотя бы один специальный символ из множества: !@#$%^&*()_-+=<>?/
# Напишите программу, которая запрашивает у пользователя пароль и затем проверяет, удовлетворяет ли он всем критериям. Если пароль удовлетворяет всем критериям, программа должна сообщить, что пароль принят. В противном случае, программа должна вывести сообщение об ошибке, указывая, какие критерии не выполняются.
user = input('enter a password: ') 

if len(user) < 8:
    raise ValueError('You password is short')
elif len([x for x in user if x.isupper()]) == 0:
    raise ValueError('you password not given uppercase')
elif len([x for x in user if x.islower()]) == 0:
    raise ValueError('you password not given lowercase')
elif len([x for x in user if x.isdigit()]) == 0:
    raise ValueError('you password not given digit')
elif len([x for x in user if x in '!@#$%^&*()_-+=<>?/']) == 0:
    raise ValueError('you password not given symbols')
else:
    print('You passoword is saved succesessfully')







    



