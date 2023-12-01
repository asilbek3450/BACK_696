from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

back_keyboard = InlineKeyboardButton(text='⬅️ Orqaga', callback_data='back')
start_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
start_keyboard.add(InlineKeyboardButton(text='📋 Menyu', callback_data='menu'))
start_keyboard.add(InlineKeyboardButton(text='📝 Biz haqimizda', callback_data='about'))
start_keyboard.add(InlineKeyboardButton(text='📞 Aloqa', callback_data='contact'))
start_keyboard.add(InlineKeyboardButton(text='💬 Kommentariy', callback_data='comment'))

menu_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(InlineKeyboardButton(text='💻 Noutbuk', callback_data='laptop'))
menu_keyboard.add(InlineKeyboardButton(text='📱 Telefon', callback_data='phone'))
menu_keyboard.add(InlineKeyboardButton(text='🎮 PS', callback_data='ps'))
menu_keyboard.add(InlineKeyboardButton(text='📦 Aksessuar', callback_data='accessory'))

contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
contact_keyboard.add(KeyboardButton(text='Telefon raqamni yuborish', request_contact=True))

laptop_keyboard = InlineKeyboardMarkup()
laptop_keyboard.add(InlineKeyboardButton(text='💻 Macbook Pro', callback_data='mack'),
                    InlineKeyboardButton(text='💻 HP', callback_data='hp'))
laptop_keyboard.add(InlineKeyboardButton(text='💻 Lenovo', callback_data='lenovo'),
                    InlineKeyboardButton(text='💻 Asus', callback_data='asus'))
laptop_keyboard.add(InlineKeyboardButton(text='💻 Dell', callback_data='dell'),
                    InlineKeyboardButton(text='💻 Acer', callback_data='acer'))
laptop_keyboard.add(back_keyboard)

phone_keyboard = InlineKeyboardMarkup()
phone_keyboard.add(InlineKeyboardButton(text='📱 iPhone 14 Pro Max', callback_data='iphone'),
                   InlineKeyboardButton(text='📱 Samsung Galaxy S22 Ultra', callback_data='samsung'))
phone_keyboard.add(InlineKeyboardButton(text='📱 Xiaomi Mi 12 Pro', callback_data='xiaomi'),
                   InlineKeyboardButton(text='📱 Huawei P60 Pro', callback_data='huawei'))
phone_keyboard.add(InlineKeyboardButton(text='📱 Nokia 10', callback_data='nokia'),
                   InlineKeyboardButton(text='📱 Sony Xperia 1 III', callback_data='sony'))
phone_keyboard.add(back_keyboard)

ps_keyboard = InlineKeyboardMarkup()
ps_keyboard.add(InlineKeyboardButton(text='🎮 PS 5', callback_data='ps5'),
                InlineKeyboardButton(text='🎮 PS 4', callback_data='ps4'))
ps_keyboard.add(InlineKeyboardButton(text='🎮 PS 3', callback_data='ps3'),
                InlineKeyboardButton(text='🎮 PS 2', callback_data='ps2'))
ps_keyboard.add(back_keyboard)

accessory_keyboard = InlineKeyboardMarkup()
accessory_keyboard.add(InlineKeyboardButton(text='📦 AirPods', callback_data='airpods'),
                       InlineKeyboardButton(text='📦 Apple Watch', callback_data='applewatch'))
accessory_keyboard.add(InlineKeyboardButton(text='📦 Samsung Watch', callback_data='samsungwatch'),
                       InlineKeyboardButton(text='📦 Mi Watch', callback_data='miwatch'))
accessory_keyboard.add(InlineKeyboardButton(text='📦 Mi Band', callback_data='miband'),
                       InlineKeyboardButton(text='📦 Samsung Galaxy Buds', callback_data='galaxybuds'))
accessory_keyboard.add(InlineKeyboardButton(text='📦 Samsung Galaxy Watch', callback_data='galaxywatch'),
                       InlineKeyboardButton(text='📦 Huawei Watch', callback_data='huaweiwatch'))
accessory_keyboard.add(InlineKeyboardButton(text='📦 JBL AirPods', callback_data='jblairpods'),
                       InlineKeyboardButton(text='📦 JBL Galaxy Watch', callback_data='jblgalaxywatch'))
accessory_keyboard.add(back_keyboard)

buy_keyboard = InlineKeyboardMarkup()
buy_keyboard.add(InlineKeyboardButton(text='🛒 Sotib olish', callback_data='buy'))
