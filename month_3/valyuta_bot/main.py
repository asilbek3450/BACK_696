import logging
import requests
from aiogram import Bot, Dispatcher, types, executor
from config import API_TOKEN

logging.basicConfig(level=logging.INFO)  # loggingni sozlaymiz

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')  # help, contact,
async def welcome(message: types.Message):
    await message.answer("Assalomu aleymum, valyuta botimizga xush kelibsiz!")


@dp.message_handler()
async def valyuta(message: types.Message):
    money = int(message.text)
    currency_code = 'USD'
    my_url = 'https://nbu.uz/uz/exchange-rates/json/'
    data = requests.get(url=my_url)

    for i in data.json():
        if i['code'] == currency_code:
            await message.answer(f'1 $ = {i["cb_price"]} so\'mga teng')
            await message.answer(f'{money} $ = {float(i["cb_price"]) * money} so\'mga teng')


if __name__ == '__main__':
    executor.start_polling(dp)
