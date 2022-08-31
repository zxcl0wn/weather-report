import requests
from datetime import *
from config import tg_bot_token, weather_token
from telebot import types
import telebot
import pytz
from time import *
import sqlite3

bot = telebot.TeleBot(tg_bot_token)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, f"Как тебя зовут?")



    @bot.message_handler(content_types=['text'])
    def greeting(message):
        global mes
        mes = message.text
        bot.send_message(message.chat.id, f"Привет, {mes}!")

        @bot.message_handler(content_types=['text'])
        def get_weather(message):
            try:
                r = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric&lang=ru"
                )
                data = r.json()

                city = data['name']
                cur_weather = data['main']['temp']
                humidity = data['main']['humidity']
                pressure = data['main']['pressure']
                wind = data['wind']['speed']
                sunrise = datetime.fromtimestamp(data['timezone'] + data['sys']['sunrise']).astimezone(
                    pytz.timezone('Etc/GMT')).strftime('%H:%M')
                sunset = datetime.fromtimestamp(data['timezone'] + data['sys']['sunset']).astimezone(
                    pytz.timezone('Etc/GMT')).strftime('%H:%M')
                type_of_weather = {
                    "Thunderstorm": 'Гроза \U0001F329',
                    "Drizzle": 'Морось \U0001F4A7',
                    "Rain": 'Дождь \U00002614',
                    "Snow": 'Снег \U00002744',
                    "Clouds": 'Облачно \U00002601',
                    "Clear": 'Ясно \U00002600',
                    "Smoke": 'Туман \U0001F32B',
                    "Mist": 'Туман \U0001F32B'
                }
                weather_discription = data['weather'][0]['main']
                if weather_discription in type_of_weather:
                    wd = type_of_weather[weather_discription]
                else:
                    wd = "FUCK YOU"
                bot.send_message(message.chat.id,
                                 f"Сейчас в городе {city} {datetime.fromtimestamp(mktime(datetime.now(pytz.timezone('Etc/GMT')).timetuple()) + data['timezone']).strftime('%H:%M')}"
                                 f"\nТемпература: {cur_weather} C°"
                                 f"\n{wd}"
                                 f"\nВлажность: {humidity} %"
                                 f"\nДавление: {pressure} мм.рт.ст"
                                 f"\nВетер: {wind} м/c"
                                 f"\nВремя рассвета: {sunrise}"
                                 f"\nВремя заката: {sunset}")

                bot.register_next_step_handler(message, get_weather)
                markup = types.InlineKeyboardMarkup()
                mark_yes = types.InlineKeyboardButton("Да")
                mark_no = types.InlineKeyboardMarkup("Нет")
                markup.add(mark_yes, mark_no)

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, f"{mes}, Такого города не существует!!!")
                bot.register_next_step_handler(message, get_weather)

        bot.register_next_step_handler(message, get_weather)

    bot.register_next_step_handler(message, greeting)






bot.polling(none_stop=True)