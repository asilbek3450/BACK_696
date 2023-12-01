import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import requests

from month_3.translate_robot.keyboards import start_keyboards, translation_buttons

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def translation(q, tilga):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": q,
        "target": tilga,
        # "source": tildan
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "0e1e80d5bfmsh213ed89c8e67ef5p10d6b3jsn0c4cbb51f1b1",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id, f'Assalom aleykum, hurmatli {message.from_user.full_name}\n'
                                            f'Tarjimon botimizga xush kelibsiz!\n', reply_markup=start_keyboards)


global_language = ''


@dp.message_handler(lambda message: message.text == '🌐 Tilni tanlash')
async def start(message: types.Message):
    await message.answer("Qaysi tilga tarjima qilish kerak: ", reply_markup=translation_buttons)


@dp.callback_query_handler()
async def languages(call: types.CallbackQuery):
    global global_language
    l_data = call.data  # uz_ru
    l = ['uz_ru', 'uz_en', 'ru_uz', 'en_uz', 'ru_en', 'en_ru']
    if l_data in l:
        global_language = l_data
        await bot.send_message(call.message.chat.id, f'Siz {l_data} ni tanladingiz')


@dp.message_handler()
async def translate(message: types.Message):
    global global_language
    if global_language != '':
        tilga = global_language.split('_')[1]
        # tildan = global_language.split('_')[0]
        q = message.text
        print(q, tilga)
        await message.answer(translation(q, tilga))

    else:
        await message.answer('Iltimos, avval tilni tanlang')


if __name__ == '__main__':
    executor.start_polling(dp)
