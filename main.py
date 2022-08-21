import requests
import telebot
from bs4 import BeautifulSoup

# Making a GET request
URL = 'http://itmydream.com/citati/duhovnost'
from config import TOKEN


def parser(url):
    r = requests.get(url)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.find_all('p')
    return [c.text for c in content]


list_of_spiry = parser(URL)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Здравия! Прикоснись к мудрости, введи любую цифру от 1 - 9:')


@bot.message_handler(content_types=['text'])
def spiry(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_spiry[0])
        del list_of_spiry[0]
    else:
        bot.send_message(message.chat.id, 'Здравия! Прикоснись к мудрости, введи любую цифру от 1 - 9:')


bot.polling()
