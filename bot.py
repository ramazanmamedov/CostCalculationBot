import telebot
import config
import random
import json_module

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('static/cat.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, 
            "Добро пожаловать, <b>{0.first_name}</b>".format(message.from_user),
            parse_mode='html',
            reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "😊 Как дела?":
            bot.send_message(message.chat.id, "Отлично!")
        else:
            bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)



