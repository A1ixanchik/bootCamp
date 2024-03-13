# 3)ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: тяжелая)
# 1. При нажатии на кнопку start, телеграмм бот должен
# зайти на сайт KaktusMedia (https://kaktus.media/) и
# спарсить категорию “Все новости”
# 2. При вводе текста должны выйти первые 20
# заголовков статей с нумерацией. Должна быть
# возможность выбрать новости по нумерации или id
# (по желанию)
# 3. После выбора новости по нумерации, телеграмм
# бот должен отправить сообщение в виде “some
# title news you can see Description of this news
# and Photo” и пользователь отправит текст (либо
# нажмет кнопку) Description, то бот должен
# отправить описание именно текущего поста, также
# аналогично с Photo.
# 4. При нажатии на кнопку «Quit» бот должен
# отправить сообщение “До свидания“
# Рекомендации:
# 1. BeautifulSoup
# 2. CSV
# 3. lxml
# 3. Requests

import telebot
from bs4 import BeautifulSoup
import requests

url = 'https://kaktus.media/?lable=8&date=2024-02-15&order=time'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
container = soup.find('div',class_='Tag--articles')
news = container.find_all('div', class_='ArticleItem')

result = {}
list_names = []
list_news = []
list_images = []
for new in news:
    name = new.find('a', class_="ArticleItem--name").text.strip()
    img = new.find('a').get('href')
    # desc = new.find('a', class_='ArticleItem--name').text.strip()
    data = {'name': name, 'img': img}
    list_names.append(name)
    

import telebot
from telebot import types
import random

token = '6884807969:AAH46lln2lVdOfYgyhrKWWG4ORkXYNzjgi0'


bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn2 = types.KeyboardButton('Name')
btn3 = types.KeyboardButton('Description')
btn4 = types.KeyboardButton('Image')
keyboard.add(btn2, btn3, btn4)


@bot.message_handler(commands=['start'])
def start_message(message):
    res = [f'{k}--> {v['name']}'for k]
    

    
bot.polling()





