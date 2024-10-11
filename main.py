import telebot
from telebot import types

bot = telebot.TeleBot('INSERT KEY HERE')


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем Web App кнопку
    web_app_url = "http://192.168.0.211:3000"  # Вставь сюда URL своего мини-приложения
    web_app = types.WebAppInfo(url=web_app_url)

    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Открыть миниапп", web_app=web_app)
    markup.add(button)

    bot.send_message(message.chat.id, "Нажми кнопку для открытия миниапп:", reply_markup=markup)


# Запуск бота
bot.polling()
