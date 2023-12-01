# with operatori
# with operatori faylni ochib ishlashni tugatganda avtomatik ravishda yopadi, close() funksiyasi shart emas

# with open('test.txt', 'r') as file:  # 'r' - read
#     print(file.read())

with open('lesson_24/test.txt', 'w') as file:  # 'w' - write
    file.write("Toxir darsga qaramayapti, bugun kurator telefon qiladi\n")

# with open('test.txt', 'a') as file:  # 'a' - append
#     file.write("Yangi qo'shildi\n")

# with open('test.txt', 'x') as file:  # 'x' - create, fayl yo'q bo'lsa yangi fayl yaratadi, bor bo'lsa xatolik beradi
#     file.write("Yangi yaratildi\n")

# with open('lesson_24/test.txt', 'r+') as file:  # 'r+' - read and write, fayl yo'q bo'lsa xatolik beradi
#     print(file.read())
#     file.write("\nYangi yozildi\n")

# with open('lesson_24/test.txt', 'w+') as file:  # 'w+' - write and read, fayl yo'q bo'lsa yangi fayl yaratadi, bor bo'lsa o'chirib boshqa yozadi
#     file.write("Yangi yozildi\n")
#     print(file.read())








# faylning joylashgan papkasini aniqlash
import os

print(os.getcwd())  # get current working directory



# faylning o'chirilishini tekshirish
# if os.path.exists('lesson_24/test.txt'):  # exists - mavjud bo'lishini tekshirish
#     os.remove('lesson_24/test.txt')  # remove - o'chirish
# else:
#     print('Fayl mavjud emas')

# faqat fayl nomini o'zgartirish
# os.rename('lesson_24/test.txt', 'lesson_24/toxir.txt')

# faylning joylashgan papkasini o'chirish
os.rmdir('lesson_23')

# faylning joylashgan papkasini yaratish
os.mkdir('lesson_23')

# Uyga vazifa

# 1. shu lesson_23 ichiga yangi homework degan papka yarating
# 2. homework ichiga 1.txt, 2.txt, 3.txt fayllarini yarating va o'z ismingizni, ota-ona ismlarini, qiziqishlaringizni 'w' orqali yozing
# 3. homework ichidagi fayllarni for yordamida with operatori orqali o'qib hammasini bittada ekranga chiqaring
# 4. homework degan papkani nomini uy_ishi degan nomga o'zgartiring
# 5. uy_ishi papkasini o'chiring
