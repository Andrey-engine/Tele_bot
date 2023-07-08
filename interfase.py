from telebot import types # для указание типов

def test(bot, message):
  bot.send_message(message.from_user.id, "123")

def help(bot, message, answer):
    bot.send_message(message.from_user.id, answer)
          

def aboutus(bot, message, answer):
    bot.send_message(message.from_user.id, answer)
   

def orderletters(bot, message, answer):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D1%81%D1%8C%D0%BC%D0%BE')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, answer, reply_markup = markup)
    
def price(bot, message, answer):
    bot.send_message(message.from_user.id, answer)    
    
    
def promotions(bot, message, answer):
    bot.send_message(message.from_user.id, answer) 

def agreement(bot, message, answer):
    bot.send_message(message.from_user.id, answer)  