import telebot
from telebot import types
import os
from dotenv import load_dotenv
load_dotenv()


bot = telebot.TeleBot(f"{os.getenv('BOT_TOKEN')}")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    web_app_url = os.getenv('NGROK_URL')
    web_app = types.WebAppInfo(url=web_app_url)

    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Открыть миниапп", web_app=web_app)
    markup.add(button)

    bot.send_message(message.chat.id, "Нажми кнопку для открытия миниапп:", reply_markup=markup)


bot.polling()
