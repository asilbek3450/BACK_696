import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import MediaGroup, ReplyKeyboardRemove, InputMedia, InputFile
from informations import laptop_info, phone_info
from config import API_TOKEN
from keyboards import start_keyboard, menu_keyboard, contact_keyboard, laptop_keyboard, phone_keyboard, ps_keyboard, \
    accessory_keyboard, buy_keyboard

API_TOKEN = API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id, f'Assalomu aleykum, {message.from_user.full_name}\n',
                           reply_markup=start_keyboard)


buy_info = ''


@dp.callback_query_handler()
async def callback_queries(call: types.CallbackQuery):
    call_data = call.data
    global buy_info
    if call_data == 'menu' or call_data == 'back':
        await bot.send_message(chat_id=call.message.chat.id, text="Menyu bo'limiga xush kelibsiz!",
                               reply_markup=menu_keyboard)
    if call_data == 'about':
        await bot.send_message(chat_id=call.message.chat.id, text="Biz haqimizda ma'lumotlar!")

    if call_data == 'contact':
        await bot.send_message(chat_id=call.message.chat.id,
                               text="Admin bilan bog'lanish uchun telefon raqam qoldiring",
                               reply_markup=contact_keyboard)

    if call_data in ['laptop', 'phone']:
        media = MediaGroup()
        for i in range(1, 7):
            media.attach_photo(photo=InputFile(f'images/{call_data}/{i}.jpg'))
        await bot.send_media_group(chat_id=call.message.chat.id, media=media)
        await bot.send_message(chat_id=call.message.chat.id, text='Birortasini tanlang', reply_markup=laptop_keyboard if call_data == 'laptop' else phone_keyboard)

    if call_data in ['mack', 'hp', 'lenovo', 'asus', 'dell', 'acer']:
        product = str(call_data)
        product_caption = laptop_info[product]['caption']
        now_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        buy_info = f'{call.message.from_user.full_name}-{now_time}\n{product_caption}\n\n'
        with open(laptop_info[product]['photo'], 'rb') as rasm:
            await bot.send_photo(chat_id=call.message.chat.id, photo=rasm, caption=product_caption,
                                 reply_markup=buy_keyboard)

    if call_data == 'buy':
        await bot.send_message(chat_id=call.message.chat.id, text='Buyurtma qabul qilindi, tez orada siz bilan bog\'lanamiz!')
        await bot.send_message(chat_id=call.message.chat.id, text="Menyu bo'limiga xush kelibsiz!", reply_markup=menu_keyboard)
        with open('buy_data.txt', 'a') as file:
            file.write(buy_info)

    if call_data in ['iphone', 'samsung', 'xiaomi', 'honor', 'huawei', 'nokia']:
        product = str(call_data)
        product_caption = phone_info[product]['caption']
        now_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        buy_info = f'{call.message.from_user.full_name}-{now_time}\n{product_caption}\n\n'
        with open(phone_info[product]['photo'], 'rb') as rasm:
            await bot.send_photo(chat_id=call.message.chat.id, photo=rasm, caption=product_caption,
                                 reply_markup=buy_keyboard)

    if call_data in ['ps2', 'ps3', 'ps4', 'ps5']:
        product = str(call_data)
        product_caption = phone_info[product]['caption']
        now_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        buy_info = f'{call.message.from_user.full_name}-{now_time}\n{product_caption}\n\n'
        with open(phone_info[product]['photo'], 'rb') as rasm:
            await bot.send_photo(chat_id=call.message.chat.id, photo=rasm, caption=product_caption,
                                 reply_markup=buy_keyboard)
if __name__ == '__main__':
    executor.start_polling(dp)
