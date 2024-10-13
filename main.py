import telebot
from telebot import types

import requests
from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(f"{os.getenv('BOT_TOKEN')}")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    web_app_url = os.getenv('NGROK_SERV_LINK')
    web_app = types.WebAppInfo(url=web_app_url)

    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Открыть миниапп", web_app=web_app)
    markup.add(button)

    bot.send_message(message.chat.id, "Нажми кнопку для открытия миниапп:", reply_markup=markup)


@bot.message_handler(commands=['go'])
def answer_with_ai(message):

    # Point to the local server
    client = OpenAI(
        organization='org-mErhxlc5Uewat376oHVa6r4h',
        project='proj_sx3dlD9yxPTFxnNVbbIARcEn',
    )
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a text conversion agent for Tarot cards. The card describes a prediction of how the user's day will go today.  Make a prediction of the day based on the card's description. Briefly describe the card, its meaning (DO NOT USE CHARACTERS). Then write the forecast itself. The forecast should be motivating and positive. DO NOT USE health and family topics. Max response length is 450 characters. You may use emojis"},
            {"role": "user", "content": "Description of the card Five of Cups: The arcana speaks of disappointment, unexpected troubles, melancholy, sadness, pain, grief for the lost. A person may experience a state of regret because his dreams and desires have not materialized, although he was counting on it so much. On the other hand, the feeling of disappointment may appear about the separation from something very important and significant. The person shows destructive emotions, emotional crisis, depression, love suffering and anger. Before a person opens a difficult period of time, although it promises a bright streak. But only if a person can cope with his problems, rather than passively suffering over them. If without end indulge in his problems, they will not go anywhere, or obsessively accompany him for a long time. And in fact, he is able to cope with his failures and difficulties, if he wishes to do so. A person is fully capable of immersing himself in his depressive thoughts, which creates even more problems for himself."}
        ],
        max_tokens=450,
        temperature=0.6,
    )

    res = completion.choices[0].message
    bot.send_message(message.chat.id, f"{res.content}")


bot.polling()
