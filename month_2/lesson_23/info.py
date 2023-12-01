# file handling

# faylni ochish va uni o'qish
# 'r' - read - o'qish, fayl yo'q bo'lsa xatolik beradi

# x = open('test.txt', 'r')
# print(x.read())
# x.close()

file = open('test.txt', 'r')
print(file.read(5))  # 5 ta belgini o'qish
print(file.read(5))  # 5 ta belgini o'qish
print(file.read(5))  # 5 ta belgini o'qish
file.close()

file = open('test.txt', 'r')
print(file.readline())  # 1-satrni o'qish
print(file.readline())  # 2-satrni o'qish
file.close()

file = open('test.txt', 'r')
for line in file:
    print(line)
file.close()

file = open('test.txt', 'r')
print(file.readlines())  # ro'yxat ko'rinishida o'qish
file.close()

# faylni yozish
# 'w' - write - yozish, fayl yo'q bo'lsa yangi fayl yaratadi, bor bo'lsa o'chirib boshqa yozadi

file = open('test.txt', 'w')
file.write('Hello world')
file.close()

file = open('test.txt', 'w')
file.write('Hello world\n')
file.write('Hello world\n')
file.write('Hello world\n')
file.close()

# 'a' - append - qo'shish, fayl yo'q bo'lsa yangi fayl yaratadi, bor bo'lsa oxiriga qo'shadi

file = open('test.txt', 'a')
file.write("Yangi qo'shildi\n")
file.close()

# 'x' - create - yaratish, fayl yo'q bo'lsa yangi fayl yaratadi, bor bo'lsa xatolik beradi

file = open('test.txt', 'x')
file.write("Yangi yaratildi\n")
file.close()

# 'r+' - read and write - o'qish va yozish, fayl yo'q bo'lsa xatolik beradi

file = open('test.txt', 'r+')
print(file.read())
file.write("Yangi yozildi\n")
file.close()

# 'w+' - write and read - yozish va o'qish, fayl yo'q bo'lsa yangi fayl yaratadi, bor bo'lsa o'chirib boshqa yozadi

file = open('test.txt', 'w+')
file.write("Yangi yozildi\n")
print(file.read())
file.close()

# Uy ishi

# 1. Nomiga ism yozilgan fayl yarating va ichidagi ma'lumotlarni 'r' orqali o'qib ekran chiqaring
# 2. info.txt nomli fayl yarating va ichiga o'z haqingizda 10 qator ma'lumotlarni 'w' orqali yozing
# 3. info.txt nomli faylga o'z haqingizdagi qiziqishlaringizni 'a' orqali qo'shing
# 4. info.txt nomli faylidagi barcha a harflarini A ga o'zgartiring
# 5. info.txt nomli fayl ichida necha qator va nechta so'zdan iborat ekanligini toping
