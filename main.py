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
import telebot
from telebot import types # для указание типов

f = open('API_iAdresat_bot.txt','r')
bot = telebot.TeleBot(f.readline());
f.close()

@bot.message_handler(commands=["start"])

def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Подробнее о нас")
    btn2 = types.KeyboardButton("Заказать письмо")
    btn3 = types.KeyboardButton("Стоимость услуг")
    btn4 = types.KeyboardButton("Акции")
    btn5 = types.KeyboardButton("Правила и соглашения")
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Мы команда...".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['button']) 
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@bot.message_handler(content_types=['text'])   

def get_text_messages(message):
    
    command = {'/help': 'вот что я могу:',  
               '/aboutus': 'Расскажем подробнее о нас…',
               '/orderletters': 'Выберите тип письма',
               '/price': '3:',
               '/promotions': '4:',
               '/agreement': '5:'}
    
    if command.get(message.text)!=None:
        bot.send_message(message.from_user.id, command.get(message.text))  
        globals()[message.text[1:]](message)
        #bot.register_next_step_handler(message, globals()[message.text[1:]]())# очень опасно надо исправить
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
def help(message):
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    print('help')

def aboutus(message):
    print('aboutus')

def orderletters(message):
    print('orderletters')

def price(message):
    print('price')    

def promotions(message):
    print('promotions') 

def agreement(message):
    print('agreement')     

    
print("work")        
bot.polling(none_stop=True, interval=1)