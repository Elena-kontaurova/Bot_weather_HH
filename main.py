import telebot
import requests
import json
from tok import TOKEN

bot = telebot.TeleBot(TOKEN)
API = 'dbf9117d63496d5232373131bc85ac4b'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветик, напиши название твоего города)')
    
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200: 
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')
        image = 'sunny.jpg' if temp > 5.0 else 'tuch.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')
        
bot.polling(none_stop = True)

# import requests 
# import re 
# from bs4 import BeautifulSoup 

# for count in range(1, 3):
#     url = f'https://eda.ru/recepty?page={count}'
#     response = requests.get(url)
    
#     bs = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    
#     tables = bs.find_all("div", attrs={'class': 'emotion-o1m2l5'}) 
    
#     for i in tables:
#         one = i.find_all('span', attrs= {'class': 'emotion-1bs2jj2'})
#         for m in one:
#             name = m.text
#             print(name) 
# if responce.status_code == 200: 
#     responce.encoding = 'windows-1251' 
#     html = responce.text 
 
#     with open(file='html.log', mode='w', encoding='utf-8') as f: 
#         f.write(html) 
 
#     responce.encoding = 'windows-1251' 
#     bs = BeautifulSoup(responce.text, features="html.parser") 
#     tables = bs.find_all("div", attrs={'class': 'emotion-o1m2l5'}) 
#     news = [] 
 
#     for new in tables: 
#         vse = new.find_all('div', attrs = {'class': 'emotion-m0u77r'})
#         for i in vse:
#             tovar = i.find_all('div', attrs = {'class': 'emotion-1f6ych6'})
#             for m in tovar:
#                 text = m.find_all('div', attrs = {'class': 'emotion-1j5xcrd'})
#                 for c in text:
#                     name = c.find('span', attrs = {'class': 'emotion-1bs2jj2'}).text
#                     print(name)
                
        # elem = new.find_all("a")[0] # for getting title and desc 
        # title, desc = elem.text, elem["title"] 
        # url = elem["href"] 
        # author = new.find("td", attrs={"class": "smalltext"}).text 
        # news.append({"title": title, "description": desc, "author": author, "url": url}) 
        # matched = re.match(r": ([A-я: ]+)\(([0-9- :]+)\)", author) 
 
        # if matched is not None: 
        #     author = matched[1] 
        #     datetime = matched[2] 
 
        #     print(author, datetime) 
        # else: 
        #     print(title, url, desc, author) 
        #     print(len(news))
