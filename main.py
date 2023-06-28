import telebot
import webbrowser
import requests
from telebot import types

bot = telebot.TeleBot('6147033652:AAFL0crQTRkPIgsrHZILlgFq_GctrsP3HEg')
amount = 0

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://t.me/izzz1')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}. Введите сумму:')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    amount = message.text.strip()
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('MNT', callback_data='get-RUB')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('RUB', callback_data='get-USD')
    btn3 = types.InlineKeyboardButton('USD', callback_data='get-MNT')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}. Выберите валюту:', reply_markup=markup)
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, f'Неверный формат.')
        bot.register_next_step_handler(message, summa)
        return


bot.polling(none_stop=True)