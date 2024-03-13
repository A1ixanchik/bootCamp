from bs4 import BeautifulSoup
import requests
import csv
import pprint

url = 'https://www.mashina.kg/search/all/'

def parsing_data(url):
    response = requests.get(url)
    # print(response.text)
    # print(type(response.text))
    soup = BeautifulSoup(response.text,'html.parser')
    container = soup.find('div', class_='table-view-list')
    cars = container.find_all('div', class_='list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_='name').text.strip()
        try:
            img = car.find('img', class_=('lazy-image-attr')).get('src')
        except Exception as e:
            img = f'N Image,{e}!'
        
        price = car.find('div', class_='block price').find('strong').text
        # print(price)
        desc = ''.join(car.find('div', class_='item-info-wrapper').text.split())
        data = {'title': name, 'desc': desc, 'price': price, 'img':img}
        result.append(data)
    return  result


def get_last_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    pages = soup.find_all('a', class_='page-link')[-1]
    return int(pages.get('data-page'))
    # print(pages)

# pprint.pprint(parsing_data(url))

def prepare_csv():
    with open('cars.csv', 'w') as file:
        fieldname = ['№', 'name', 'desc', 'price', 'img']
        writer = csv.DictWriter(file, fieldname)
        writer.writerow({
            '№': '№',
            'name': 'Name:',
            'desc': 'Description:',
            'price': 'Price',
            'img': 'Image Url'
        })
def write_to_csv(data: list):
    with open('cars.csv', 'a') as file:
        global count
        fieldname = ['№', 'name', 'desc', 'price', 'img']
        writer = csv.DictWriter(file, fieldname)
        for car in data:
            writer.writerow({
                '№': count,
                'name': car['title'],
                'desc': car['desc'],
                'price': car['price'],
                'img': car['img']
            })
            count += 1


prepare_csv()
count = 1  
data = parsing_data(url)
write_to_csv(data)  
last_page = get_last_page(url)
print(last_page)
i = 1
while i <= last_page:
    page_url = f'https://m.mashina.kg/search/all/?page={i}' 
    data = parsing_data(page_url)
    write_to_csv(data)
    print(f'Спарсили {i} / {last_page} страницу!')   
    i += 1

