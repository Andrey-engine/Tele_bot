# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:07:16 2023

@author: android
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os # для сервера
from background import keep_alive #импорт функции для поддержки работоспособности
# import pip
# pip.main(['install', 'pytelegrambotapi'])

import telebot
from telebot import types # для указание типов


from pathlib import Path # пути к файлам
import codecs
from interfase import *

bot = telebot.TeleBot(os.getenv("API_iAdresat_bot"))

@bot.message_handler(commands=["start"])
def start(message, res=False):
       
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton("Подробнее о нас") # создать связь со словорём
    btn2 = types.KeyboardButton("Заказать письмо")
    btn3 = types.KeyboardButton("Стоимость услуг")
    btn4 = types.KeyboardButton("Акции")
    btn5 = types.KeyboardButton("Правила и соглашения")
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Добро пожаловать в чат-бот компании «ЯАдресат», которая отправляет неожиданные бумажные письма! Выберите интересующий Вас раздел.".format(message.from_user), reply_markup=markup)
    

bot = telebot.TeleBot(os.getenv("API_iAdresat_bot"))

@bot.message_handler(content_types=['text'])   

def get_text_messages(message):
    button = {'/aboutus':'/aboutus', # переделать
              '/orderletters':'/orderletters',
              '/price': '/price',
              '/promotions':'/promotions',
              '/agreement':'/agreement',
              
              'Подробнее о нас':'/aboutus',
              "Заказать письмо"  : '/orderletters',
              "Стоимость услуг"  : '/price',
              "Акции" : '/promotions',
              "Правила и соглашения": '/agreement'}

    if button.get(message.text)!=None:
        func = button.get(message.text)[1:]
        globals()[func](bot, message, file_txt(func + '.txt') )  # не корректный вызов функции
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
  

def file_txt(name_file):# добавить обработку ошибок
    path = Path("message", name_file)
    with codecs.open(path, 'r', encoding='utf-8') as file:
        read_file = file.read()
    return read_file

          
keep_alive()
bot.infinity_polling()
#bot.polling(none_stop=True, interval=1)