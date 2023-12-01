
# O'tiladigan mavzular:
#
# - Funksiya mavzusini takrorlash
# - Argument va parametrlar
#
#
# Masalalar:
#
# 1. Ikkita parametr qabul qiladigan funksiya yozing ikka parametr ham int bolsin
#    u funksiya usha ikkala sonni 2-darajaga oshirib bir birga qoshib qayytarib bersin
#
# 2. Ikkita parametr qabul qiladigan funksiya yozing. Birinchisi int ikkinchisi str bolsin
#    u funksiya str ni ichidagi unli harflar sonini topib 1-parametrga kopaytirib natijani
#    qaytarish

def int_multiply_str(son:int, matn: str):
    unlilar = 'aeiou'
    count = 0
    for i in matn:
        if i in unlilar:
            count += 1
    return son * count

print(int_multiply_str(10, 'asilbek'))


# 3. 3 ta parametr qabul qiladigan funksiya yozing. Uchchalasi ham int bolsin.
#    U funksiya 3 ta sondan eng kattasini qaytarib bersin.
#
# 4. Ikkita parametr qabul qiladigan funksiya yozing. 1-int 2-str bolsin.
#    str ni ichidagi undosh harflar sonidan unli harflar sonini ayiring va
#    1-parametrga qoshib qaytarib bering.
#
# 5. 5 ta parametr qabul qiladigan funksiya yozing. Barchasi int bo'lsin.
#    Ularni ichidan eng katta va eng kichkinasini list ichiga solib qaytarib bering,


# Sinf ishi + uy ishi
# list va dict metodlarini def qilib yaratish

# 1. listni parametr qilib olib, listni o'zini teskari tartibda qaytaruvchi funksiya yarating
# 2. List uchun element qo'shish, o'chirish, tahrirlash funksiyalarini yarating. Ularning nomlari add_element, remove_element, edit_element deb nomlangan bo'lsin.
#    Buning uchun listni o'zini va qo'shiladigan o'chiriladigan yoki tahrirlanadigan elementni parametr qilib oling.
#    Misol uchun def add_element(mylist, element):, def remove_element(mylist, element):, def edit_element(mylist, element, new_element): bo'lsin.

# 1. Dictni parametr qilib olib, "dict[key] ning qiymati - dict[value]" ko'rinishida qaytaruvchi funksiya yarating 2.
# Davlat nomi-poytaxt-aholi soni lug'atini yarating. Keyin funksiya yaratasiz u funksiyaga foydalanuvchi input orqali
# davlat nomini kiritganda shu davlat haqida ma'lumotlarini chiqarib bersin. Misol uchun "O'zbekiston poytaxti
# Toshkent shahri, aholisi 34 000 000" bo'lsin.











