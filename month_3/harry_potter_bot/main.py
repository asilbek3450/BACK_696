import aiogram
import logging

import requests

from aiogram import Bot, Dispatcher, types, executor

from config import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)  # loggingni sozlaymiz

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer(f'Assalomu aleykum {message.from_user.full_name}\n'
                         f'Harry Potter qahramonlari haqida ma\'lumot botiga xush kelibsiz')


@dp.message_handler()
async def info(message: types.Message):
    my_url = 'https://hp-api.onrender.com/api/characters'
    data = requests.get(url=my_url)
    data = data.json()
    my_data = {}
    ism = message.text.title()
    for i in data:
        my_data[i['name']] = f"""
Ismi: {i['name']},
Hayotdagi ismi: {i['actor']}
Tug'ilgan yili: {i['dateOfBirth']}
Guruhi: {i['house']}
        """
    bor = False
    for i in data:
        if ism == i['name']:
            bor = True
            rasm = i['image']
            await message.answer_photo(photo=rasm, caption=my_data[ism])

    if bor == False:
        await message.answer("Bunday odam yo'q")

if __name__ == '__main__':
    executor.start_polling(dp)
