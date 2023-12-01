import logging
import wikipedia

from aiogram import Bot, Dispatcher, types, executor
from config import API_TOKEN

logging.basicConfig(level=logging.INFO)  # loggingni sozlaymiz

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# wikipedia.set_lang('uz')


@dp.message_handler(commands='start')  # help, contact, wikipedia
async def welcome(message: types.Message):
    await message.answer("Assalomu aleymum, wikipedia botimizga xush kelibsiz!")


# uz yaxshi qiz bola
# ru яблоко
@dp.message_handler()
async def wiki(message: types.Message):
    til = message.text.split()[0]
    q = ''.join([x + ' ' for x in message.text.split()[1:]])  # listni stringga qo'shib ketadi
    if til == 'uz':
        wikipedia.set_lang('uz')
    elif til == 'ru':
        wikipedia.set_lang('ru')
    elif til == 'en':
        wikipedia.set_lang('en')
    else:
        await message.answer('Til noto\'g\'ri yozildi')
    try:
        response = wikipedia.summary(q)
        await message.answer(response)
    except:
        await message.answer("Natija topilmadi!!!!")


if __name__ == '__main__':
    executor.start_polling(dp)
