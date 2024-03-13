# JSON - JavaScript Object Notation
# Единый текстовый формат данных, был создан для хранения и передачи данных между сервисами, проектами 
# <fileName>.json файл в формате JSON
# {
#     "id": 1,
#     "author":{
#         "name": "Ed Sheran",
#         "age": 35,
#     },

# }
# Процессы Сериализации и Десериализации данных (конвертация)



# Сериализация (запись данных в JSON) - Это перевод из Python в JSON формат
# dump - записывает данные в файл формаьа JSON
# dumps - записывает данные в текст формата JSON

# Десериализация (чтение данных из JSON) - Это процес перевода из JSON  в PY dict

# load - функция которая считывает данные из файла JSON
# loads - функция которая считывет данные из текста JSON

#--------------------------------
# процесс сериализации

# import json

# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_, type(dict_))
# json_text = json.dumps(dict_ )
# print()
# print(json_text, type(json_text))

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)



# ---------------------------------
# процес десериализации
# import json
# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data,type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))

import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))




