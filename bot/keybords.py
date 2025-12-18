from telebot import types


def get_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Конвертировать валюту", "Курсы валют")
    markup.add("Настройки", "Помощь")
    return markup


def get_currency_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("USD", "EUR", "RUB")
    markup.add(" Назад")
    return markup
