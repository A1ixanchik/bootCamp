# 2)ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя)
# ● Спарсить kolesa.kz, категорию:
# 1.Название всех моделей.
# 2.Цену всех моделей
# 3.Изображение всех моделей
# 4.Краткое описание всех моделей
# 5.Записать все в csv файл

# Анвар king, [15 Feb 2024 at 12:21:36]:
# Ребят вместо колес парсите https://auto312.kg/ вытащите цену, описание, фотки, номер продавца


from bs4 import BeautifulSoup
import requests
import csv
import lxml

url = 'https://auto312.kg/'
html_text = requests.get(url)
soup = BeautifulSoup(html_text.text, 'lxml')
container = soup.find('div', class_="dj-items-rows")
car = container.find_all('div', class_="item_row_in")

result = []
for cars in car:
    name = cars.find('div', class_="item_title").text.strip()
    img = cars.find('img', class_="" ).get('src')
    price = cars.find('div', class_="item_price").text.strip()
    desc = cars.find('div', class_='item_content_in').text.strip()
    data = {'name': name, 'price': price, 'desc': desc, 'img':'https://www.//auto312.kg' + img}
    result.append(data)

print(result)
for item in result:
    print(item)

def prepare_csv():
    with open('auto.csv', 'w') as file:
        fieldnames = ['№', 'name', 'img','desc','price']
        writer =csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'name': 'Name:',
            'img': 'Image Url:',
            'desc': 'desc',
            'price': 'Price:',
        })
def write_to_scv(data, count):
    with open('auto.csv', 'a') as file:
        # global count
        fieldnames = ['№', 'name', 'img','desc','price']
        writer =csv.DictWriter(file, fieldnames)
        for auto in data:
            writer.writerow({
                '№': count,
                'name':  auto['name'],
                'price': auto['price'],
                'desc': auto['desc'],
                'img': auto['img'],
                
            })
            count += 1
    return count
 
count = 1
prepare_csv()
count = write_to_scv(result, count)












