"""Functions
Funksiya bu biror bir amalni bajaruvchi kod bloki.

Funksiyalarni yaratish uchun def kalit so'zi va funksiya nomi yoziladi.
def funksiya_nomi():
    funksiya_tanasi

Funksiyalarni chaqirish uchun funksiya nomi yoziladi va () qo'yiladi.

funksiya_nomi()

"""

# def salom_ber():
#     print("Assalomu aleykum, Xush kelibsiz")
# salom_ber()


# 1
# a = 45
# b = 72
# c = 72
#
# def eng_katta():
#     if a > b and a > c: # agar
#         print(f"Eng kattasi {a}")
#     elif b > a and b > c: # yoki
#         print(f'Eng kattasi {b}')
#     elif c > a and c > b:
#         print(f'Eng kattasi {c}')
#     else:
#         print("Eng kattasi yo'q, teng bo'lib qolgan")
# eng_katta()
#


# 2
sonlar = [6, 1, 10, 213, 62, 99]


def summa():
    total = 1
    for i in sonlar:
        total += i
    return total


print(summa())

"""
Funksiyalarga parametrlari va argumentlari yozilishi mumkin.

- Parametrlar funksiya nomi yozilganidan so'ng () ichida yoziladi.
def funksiya_nomi(parametr1, parametr2):
    funksiya_tanasi

- Argumentlar funksiya chaqirilganda () ichida yoziladi.
funksiya_nomi(argument1, argument2)
"""

# Misollar
# 1. Uchta sonning eng kattasini topib beradigan funksiyasi yozing.
# 2. Ro'yxatdagi sonlarni yig'indisini topadigan funksiya yozing.
# 3. Ro'yxatdagi sonlarni ko'paytmasini topadigan funksiya yozing.
# 4. Matnni teskari tartibda chiqaruvchi funksiya yozing.
# 5. x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# 6. Biror son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.


# Funksiyalarga parametr berib uqoridagi narsalarni foydalanuvchidan olib argument sifatida ishlash
