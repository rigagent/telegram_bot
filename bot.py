#! /usr/bin/env python
# -*- coding: utf-8 -*-

import config
import telebot
from telebot import *
from movies import *

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["help"])
def start_message(message):
    bot.send_message(message.chat.id, "Используйте '/movies' команду...")


@bot.message_handler(commands=["movies"])
def movies(message):
    movies = get_movies()
    for movie in movies:
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text=movies[movie], url=movies[movie])
        keyboard.add(url_button)
        bot.send_message(message.chat.id, movie, reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()
