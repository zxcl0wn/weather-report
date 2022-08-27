import requests
from datetime import *
from config import tg_bot_token, weather_token
from telebot import types
import telebot

bot = telebot.TeleBot(tg_bot_token)
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Напиши название города и я отправлю информацию о погоде в этом городе!")

# @bot.message_handler(content_types=["Да"])
# def yes_answer(message):
#     await message.reply(f"")

@bot.message_handler()
def get_weather(message):
    try:
        r = requests.get(
             f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
        lenth_of_the_day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(data['sys']['sunrise'])
        type_of_weather = {
            "Thunderstorm": 'Гроза \U0001F329',
            "Drizzle": 'Морось \U0001F4A7',
            "Rain":  'Дождь \U00002614',
            "Snow": 'Снег \U00002744',
            "Clouds": 'Облачно \U000026C5',
            "Clear": 'Ясно \U00002600',
            "Smoke": 'Туман \U0001F32B'
        }
        weather_discription = data['weather'][0]['main']
        if weather_discription in type_of_weather:
            wd = type_of_weather[weather_discription]
        else:
            wd = "FUCK YOU"
        # f"Сегодня: {datetime.now().strftime('%Y/%m/%d %H:%M')}"
        bot.send_message(message.chat.id, f"\nПогода в городе {city}"
              f"\nТемпература: {cur_weather} C°"
              f"\n{wd}"
              f"\nВлажность: {humidity} %"
              f"\nДавление: {pressure} мм.рт.ст"
              f"\nВетер: {wind} м/c"
              f"\nВремя рассвета: {sunrise}"
              f"\nВремя заката: {sunset}"
              f"\nПродолжительность дня: {lenth_of_the_day}")
        markup = types.InlineKeyboardMarkup()
        mark_yes = types.InlineKeyboardButton("Да")
        mark_no = types.InlineKeyboardMarkup("Нет")
        markup.add(mark_yes, mark_no)
        bot.send_message(message.chat.id, f"Какой-то другой город?", reply_markup=markup)

    except Exception as ex:
        # print(ex)
        bot.send_message(message.chat.id, "Такого города не существует")

bot.polling(none_stop=True)
