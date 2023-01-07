import time
import telebot
from telebot import types

bot = telebot.TeleBot('5833589689:AAEWS3ZpVbP29jyX0MYsrcRX0VWDFTo-bMY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>!' \
           f'\nЯ — бот-помощник в готовке стейков🥩'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    menu = 'Давай определимся, что будем готовить:'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ribeye = types.InlineKeyboardButton('Рибай', callback_data='Ribeye')
    new_york = types.InlineKeyboardButton('Нью-Йорк', callback_data='NewYork')
    info = types.InlineKeyboardButton('Информация о стейках')
    mainMenu = types.InlineKeyboardButton('Главное меню')
    markup.add(ribeye, new_york, info, mainMenu)
    bot.send_message(message.chat.id,
                     menu,
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Рибай':
        photo = open('img/ribeye.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)

        text = open('txt/Ribeye.txt', 'r', encoding='utf-8')
        bot.send_message(message.chat.id,
                         text.read(-1),
                         parse_mode='html')
        text_d = open('txt/Ribeye.rtf', 'rb')
        bot.send_document(message.chat.id, text_d)
    elif message.text == 'Информация о стейках':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        types_of = types.KeyboardButton('Виды стейков')
        fry_types = types.KeyboardButton('Виды прожарки')
        main_menu = types.KeyboardButton('Главное меню')
        markup.add(types_of, fry_types, main_menu)
        bot.send_message(message.chat.id,
                         'Какая информация тебя интересует?',
                         reply_markup=markup)
    elif message.text == 'Виды стейков':
        photo = open('img/steak_origin.png', 'rb')
        bot.send_photo(message.chat.id, photo)

        bot.send_message(message.chat.id,
                         'Держи памятку, из каких частей коровы делаются какие стейки🐄',
                         parse_mode='html')
    elif message.text == 'Виды прожарки':
        photo = open('img/fry_types.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)

        bot.send_message(message.chat.id,
                         'Держи памятку о степенях прожарки стейков🔥',
                         parse_mode='html')
    elif message.text == 'Нью-Йорк':
        bot.send_message(message.chat.id,
                         'Трудимся в поте лица, чтобы поделиться рецептом🛠',
                         parse_mode='html')
    elif message.text == 'Главное меню':
        start(message)
    else:
        bot.send_message(message.chat.id,
                         'Я тебя не понимаю 😞\nПопробуй воспользоваться командой из меню👇' ,
                         parse_mode='html')


bot.polling(none_stop=True)
