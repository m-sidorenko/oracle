import json

from openai import OpenAI

from fastapi import FastAPI

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
cards_list: dict = {}
with open('/Users/mikhail/PycharmProjects/mini-app_demo/back_end/app/cards.json') as f:
    cards_list = json.load(f)


client = OpenAI(
        organization=os.getenv('OPEN_AI_ORG_ID'),
        project=os.getenv('OPEN_AI_PROJECT'),
        api_key=os.getenv('OPEN_AI_KEY')
)


def get_tuned_card_text(card_name: str, card_text: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Ты агент, занимающийся преобразованием текста для карт Таро. Карта описывает прогноз, "
                           "как пройдет сегодняшний день пользователя.  Составь прогноз дня исходя из описания карты. "
                           "Кратко опиши карту, ее значение (НЕ ИСПОЛЬЗУЙ ЗАГОЛОВКИ). Затем напиши сам прогноз. "
                           "Прогноз должен быть мотивирующий и позитивный. НЕ ИСПОЛЬЗУЙ темы здоровья и семьи. "
                           "Макс.длина ответа 450 символов. Можно использовать emojis"
            },

            {
                "role": "user",
                "content": f"Описание карты {card_name}: {card_text}"
            }
        ],
        max_tokens=450,
        temperature=0.7,
    )
    return completion.choices[0].message.content


@app.get("/")
def read_root():
    return {"message": "Welcome to the API root!"}


@app.get("/get_card_text")
async def get_tarot_card_text(card_id: int):
    if cards_list:
        if card_id in [item['id'] for item in cards_list]:
            ai_text = get_tuned_card_text(cards_list[card_id]["name"], cards_list[card_id]["descriptionGeneral"])
            return {
                "card_id": card_id,
                "name": cards_list[card_id]["name"],
                "image_link": cards_list[card_id]["image"],
                "card_text": ai_text,
            }
        else:
            return {
                "ERROR: card_id is not valid"
            }
# class Tarot:
#     # Point to the local server
#     client = OpenAI(
#         organization='org-mErhxlc5Uewat376oHVa6r4h',
#         project='proj_sx3dlD9yxPTFxnNVbbIARcEn',
#         api_key=os.getenv('OPEN_AI_KEY')
#     )
#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system",
#              "content": "You are a text conversion agent for Tarot cards. The card describes a prediction of how the user's day will go today.  Make a prediction of the day based on the card's description. Briefly describe the card, its meaning (DO NOT USE CHARACTERS). Then write the forecast itself. The forecast should be motivating and positive. DO NOT USE health and family topics. Max response length is 450 characters. You may use emojis"},
#             {"role": "user",
#              "content": "Description of the card Five of Cups: The arcana speaks of disappointment, unexpected troubles, melancholy, sadness, pain, grief for the lost. A person may experience a state of regret because his dreams and desires have not materialized, although he was counting on it so much. On the other hand, the feeling of disappointment may appear about the separation from something very important and significant. The person shows destructive emotions, emotional crisis, depression, love suffering and anger. Before a person opens a difficult period of time, although it promises a bright streak. But only if a person can cope with his problems, rather than passively suffering over them. If without end indulge in his problems, they will not go anywhere, or obsessively accompany him for a long time. And in fact, he is able to cope with his failures and difficulties, if he wishes to do so. A person is fully capable of immersing himself in his depressive thoughts, which creates even more problems for himself."}
#         ],
#         max_tokens=450,
#         temperature=0.6,
#     )
#
#     res = completion.choices[0].message
#     print(res)
