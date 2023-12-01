import logging

from aiogram import Bot, Dispatcher, executor, types  # kutubxonalarni chaqirib olish

API_TOKEN = '6575520266:AAGDjH_XliDTzBfj0WhaAihokHHdUWJ5GfM'  # kalit

# Configure logging
logging.basicConfig(level=logging.INFO)  # loggingni sozlaymiz

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)  # bot yaratish*
dp = Dispatcher(bot)  # aloqani boshqarib turadi


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Assalomu aleykum botimga xush kebsan !!!")


@dp.message_handler(commands='help')
async def start(message: types.Message):
    await message.answer("Yordam uchun admin: @mirolimov_a !!!")


@dp.message_handler(commands='samsung')
async def send_samsung(message: types.Message):
    await message.answer_photo('https://abusaxiy.top/wp-content/uploads/2023/02/1.jpg', caption='rasm tagidagi yozuv')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f'Siz buni yozdingiz:\n{message.text}')


if __name__ == '__main__':  # bot ni ishlatish uchun
    executor.start_polling(dp, skip_updates=True)
