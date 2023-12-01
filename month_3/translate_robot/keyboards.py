from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

home_button = KeyboardButton('🏠 Bosh sahifa')
language_button = KeyboardButton('🌐 Tilni tanlash')
help_button = KeyboardButton('❓ Yordam')
contact_button = KeyboardButton('📞 Aloqa')
back_button = KeyboardButton('⬅️ Orqaga')

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
start_keyboards.add(home_button, language_button)
start_keyboards.add(help_button, contact_button, back_button)

contact = KeyboardButton('Telefon raqamni yuborish', request_contact=True)
contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
contact_keyboard.add(contact, back_button)


translation_buttons = InlineKeyboardMarkup(row_width=3)
translation_buttons.add(InlineKeyboardButton('uzb->english', callback_data='uz_en'), InlineKeyboardButton('english->uzb', callback_data='en_uz'), InlineKeyboardButton('rus->uzb', callback_data='ru_uz'))
translation_buttons.add(InlineKeyboardButton('uzb->rus', callback_data='uz_ru'), InlineKeyboardButton('rus->enlish', callback_data='ru_en'), InlineKeyboardButton('english->rus', callback_data='en_ru'))
