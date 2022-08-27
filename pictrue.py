# python main.py
from telebot import types
import telebot
from random import *

bot = telebot.TeleBot('5584052547:AAFDT20KX_4QVfbEPH7Fz9kaE1uAMoVY0_Q')  # токен

@bot.message_handler(commands=['start'])  # работает при команде(/) start
def start(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)  # отправить сообщение, к-е хранится в переменной, в чат


# @bot.message_handler(content_types=['text'])  # работает при любом  текстовом сообщении
# def get_user_text(message):
#     if message.text == 'привет':
#         bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
#     elif message.text == "айди":
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}")
#     elif message.text == 'фото':
#         photoKQ = open('KillerQueen_ASB.webp', 'rb')  # распаковка фото
#         photoKC = open('King_Crimson.webp', 'rb')
#         photoMiH = open('Made_in_Heaven_Infobox_Manga.webp', 'rb')
#         zxc = [photoKQ, photoKC, photoMiH]
#         bot.send_photo(message.chat.id, choice(zxc))  # отправляет фото

@bot.message_handler(content_types=['photo'])  # работает при фотографии
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Fuck you')  # отправляет сообщение в чат в ответ на фото


@bot.message_handler(commands=['website'])  # работает при команде(/) website
def website(message):
    markup = types.InlineKeyboardMarkup()  # создаёт поле у сообщения для кнопок
    mark1 = types.InlineKeyboardButton('Посетить gay web site', url="https://scryfall.com/")  # кнопка
    markup.add(mark1)  # добавление кнопки в поле
    bot.send_message(message.chat.id, 'Nice dick', reply_markup=markup)  # отправление сообщения в чат с кнопкой

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # кнопка внизу строки; подходящий размер;
    website = types.KeyboardButton('Веб сайт')  # кнопка 1
    start = types.KeyboardButton('Старт')  # кнопка 2
    markup.add(website, start)  # добавление вниз строки 2х кнопок
    bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)
    message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())



bot.polling(none_stop=True)  # постоянная работа бота