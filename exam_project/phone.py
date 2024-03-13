
# 1)ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: легкая)
# Вы должны спарсить сайт
# https://www.kivano.kg/mobilnye-telefony. Как результат вы должны
# получить:
# 1. Наименование всех телефонов
# 2. Цену каждого продукта(в KGS)
# 3. И ссылка к фотографии
# 4. Все это записать в CSV файл
# Дополнительно(по желанию):
# 1. Ваш парсинг скрипт должен выполняться каждые 60 минут

from bs4 import BeautifulSoup
import requests
import csv
import lxml

url = 'https://www.kivano.kg/mobilnye-telefony'
html = requests.get(url)
# def parsing_phone(url):
# response = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
# print(soup)
container = soup.find('div', class_="product-index product-index oh")
phones = container.find_all('div', class_="item product_listbox oh")
print(container)
result = []
for phone in phones:
    name = phone.find('div', class_="listbox_title oh").text.strip()
        # print(name)
    img = phone.find('img', class_="" ).get('src')
    price = phone.find('div', class_="listbox_price text-center").text.strip()
    data = {'name': name, 'price': price, 'img':'https://www.kivano.kg' + img}
    result.append(data)

    
# for item in result:
        # print(item)
    # return result

# print(parsing_phone(url))

# def prepare_csv():
#     with open('mobilka.csv', 'w') as file:
#         fieldnames = ['№', 'name', 'img', 'price']
#         writer =csv.DictWriter(file, fieldnames)
#         writer.writerow({
#             '№': '№',
#             'name': 'Name:',
#             'img': 'Image Url:',
#             'price': 'Price:',
#         })
# def write_to_scv(data, count):
#     with open('mobilka.csv', 'a') as file:
#         # global count
#         fieldnames = ['№', 'name', 'img', 'price']
#         writer =csv.DictWriter(file, fieldnames)
#         for mobilka in data:
#             writer.writerow({
#                 '№': count,
#                 'name':  mobilka['name'],
#                 'price': mobilka['price'],
#                 'img': mobilka['img']
#             })
#             count += 1
#     return count
 
# count = 1
# prepare_csv()
# count = write_to_scv(result, count)
