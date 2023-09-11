# list with function

# 1. Bitta funksiya yarating, unga start va end degan 2 ta parametr berib, start dan end gacha bo'lgan sonlar
#   ro'yxatini return qilsin. Huddi range qilgan ishni bajarsin.
#
# def oraliq(start, end, step=1):
#     sonlar = []
#     i = start
#     while i <= end:
#         sonlar.append(i)
#         i = i + step
#
#     return sonlar
#
#
# result = oraliq(5, 100, 10)
# print(result)
# # print(oraliq(10, 100, 10, 5))
#
#
# def malumotlar(*malumot):
#     return malumot
#
# result = malumotlar('12345', 1234567)
# print(result)
# print(type(result))


# 2. Yangi baholash degan funksiya yarating. U parametr sifatida o'quvchilar ismlaridan iborat list qabul qiladi.
# Funksiya ishlaganda har bir o'quvchi ismini konsolga chiqaradi va shu o'quvchiga baho qo'yishni input qilib
# so'raydi. Natijani dict ko'rinishida return bilan qaytaradi. (key=ism, value=baho) Yuqoridagi funksiyani chaqirib,
# natijani result ga o'zlashtiring.


# *args bu - functionni parametrlarini istalgancha berish uchun ishlatiladi,
# natijada tuple ko'rinishida qaytariladi

# def malumotlar(*malumot):
#     return malumot

# def min_max(*sonlar):
#     print(f'Minimal son: {min(sonlar)}')
#     print(f'Maksimal son: {max(sonlar)}')
#
#
# min_max(23456, 3462, 123120)


# **kwargs - functionni parametrlarini istalgancha berish uchun ishlatiladi,
#            faqat bunda funksiya chaqirilganda parametrlar nomi bilan beriladi,
#            natijada dict ko'rinishida qaytariladi

def students(**info):
    # print(info)
    for key, value in info.items():
        print(f'{key} - {value}')


students(ismi='Zubayr', coins=100, familiyasi='Nematjonov', yoshi=30)

# Foydalanuvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili, telefon raqami kiritishni
# so'rang. Kiritilgan ma'lumotlarni dictionary ko'rinishida qaytarib beruvchi funksiya yarating. Ma'lumotlarni
# konsolga chiqarib beruvchi funksiya yarating.


# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key.title()}: {value}")
#
#
# info(name="Ali", surname="Valiyev", year=1990, city="Tashkent", email="alivaliyev@gmail.com", phone="+998901234567")
