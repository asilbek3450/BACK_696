import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentType, InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class RegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()
    username = State()
    user_id = State()


@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer(f'Xush kelibsiz {message.from_user.full_name}')


@dp.message_handler(commands='register')
async def register(message: types.Message):
    await message.answer("Registratsiyaga xush kelibsiz, ismingizni kiriting: ")
    await RegisterState.first_name.set()


@dp.message_handler(state=RegisterState.first_name)
async def register_f(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Familiyangizni kiriting: ")
    await RegisterState.last_name.set()


phone_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Telefon raqam jo'natish", request_contact=True))


@dp.message_handler(state=RegisterState.last_name)
async def register_f(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Telefon raqamingizni kiriting: ", reply_markup=phone_keyboard)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=[ContentType.CONTACT, ContentType.TEXT])
async def phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number if message.contact else message.text)
    await message.answer("Username kiriting: ")
    await RegisterState.username.set()


@dp.message_handler(state=RegisterState.username)
async def username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.update_data(user_id=message.from_user.id)
    data = await state.get_data()
    await message.answer(f"Ma'lumotlar:\n"
                         f"Ism: {data['first_name']}\n"
                         f"Familiya: {data['last_name']}\n"
                         f"Telefon raqam: {data['phone_number']}\n"
                         f"Username: {data['username']}\n"
                         f"User_id: {data['user_id']}\n\n"
                         f"Ro'yxatdan o'tish uchun /register ni bosing")


calculator_keyboards = InlineKeyboardMarkup(row_width=4)

calculator_keyboards.add(InlineKeyboardButton('AC', callback_data='clear'),
                         InlineKeyboardButton('+/-', callback_data='plus_minus'),
                         InlineKeyboardButton('%', callback_data='%'),
                         InlineKeyboardButton('/', callback_data='oper:/'))

calculator_keyboards.add(InlineKeyboardButton('7', callback_data='number:7'),
                         InlineKeyboardButton('8', callback_data='number:8'),
                         InlineKeyboardButton('9', callback_data='number:9'),
                         InlineKeyboardButton('X', callback_data='oper:*'))

calculator_keyboards.add(InlineKeyboardButton('4', callback_data='number:4'),
                         InlineKeyboardButton('5', callback_data='number:5'),
                         InlineKeyboardButton('6', callback_data='number:6'),
                         InlineKeyboardButton('-', callback_data='oper:-'))

calculator_keyboards.add(InlineKeyboardButton('1', callback_data='number:1'),
                         InlineKeyboardButton('2', callback_data='number:2'),
                         InlineKeyboardButton('3', callback_data='number:3'),
                         InlineKeyboardButton('+', callback_data='oper:+'))

calculator_keyboards.add(InlineKeyboardButton('0', callback_data='number:0'),
                         InlineKeyboardButton('', callback_data='.'),
                         InlineKeyboardButton('=', callback_data='='))


class CalculatorState(StatesGroup):
    number1 = State()
    number2 = State()
    operation = State()


@dp.message_handler(commands='calculator')
async def calculator(message: types.Message):
    await message.answer("Calculatorga xush kelbsiz!", reply_markup=calculator_keyboards)
    await CalculatorState.number1.set()


@dp.callback_query_handler(state=CalculatorState.number1)
async def numbers(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    await state.update_data(number1=data.split(':')[-1])
    await bot.send_message(chat_id=call.from_user.id, text=data)
    await CalculatorState.operation.set()


@dp.callback_query_handler(state=CalculatorState.operation)
async def numbers(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    await state.update_data(operation=data.split(':')[-1])
    await bot.send_message(chat_id=call.from_user.id, text=data)

    await CalculatorState.number2.set()


calc_data = {}


@dp.callback_query_handler(state=CalculatorState.number2)
async def numbers(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    global calc_data
    await state.update_data(number2=data.split(':')[-1])
    await bot.send_message(chat_id=call.from_user.id, text=data)
    calc_data = await state.get_data()
    await state.finish()


@dp.callback_query_handler(text='=')
async def calc(call: types.CallbackQuery):
    data = call.data
    global calc_data
    num1 = int(calc_data['number1'])
    num2 = int(calc_data['number2'])
    summa = num1 + num2
    await bot.send_message(chat_id=call.from_user.id, text=f'{calc_data}')
    await bot.send_message(chat_id=call.from_user.id, text=f'{num1} {num2}')

    if calc_data['operation'] == '+':
        await bot.send_message(chat_id=call.from_user.id, text=summa)


if __name__ == '__main__':
    executor.start_polling(dp)
