# # fayldan o'qish uchun: 'r', agar file yo'q bo'lsa xatolik beradi ERROR

fayl = open('lesson_23/main.py', 'r')  # mode = read
print(fayl.read())
fayl.close()

# yangi = open('mars.txt', 'r')
# print(yangi.readline())
# print(yangi.readline())
# print(yangi.readline())
# yangi.close()

# fayl = open('mars.txt', 'r')
# for line in fayl:
#     print(fayl.readline())
# fayl.close()

# fayl = open('mars.txt', 'r')
# print(fayl.readlines())  # list qiberadi
# fayl.close()


# faylga yozish uchun: 'w' - write(), agar fayl bor bo'lsa o'chirib yangi yozadi, agar yo'q bo'lsa yangi yaratadi
                                

fayl = open('lesson_23\kamron.txt', 'w')
fayl.write('Kamron etiborsiz bola darsga qaramayapti')
fayl.write("\nqo'lini qirsillatib o'tiribdi")
fayl.close()

# # faylga qo'shish uchun: 'a' - append, agar bor bo'lsa yonidan qo'shib ketadi, yo'q bo'lsa yaratib yozib beradi

# fayl = open('lesson_23\kamron.txt', 'r')
# fayl.write('\nYangi gap yozdim')
# fayl.close

# fayl = open('lesson_23\Toxir.txt', 'a')
# fayl.write("Toxir dars qimayapti, otasiga telefon qilish kere")
# fayl.close()


# info.txt fayl yaratasizlar. 
# 1. fayl ichiga o'zilar haqilarda ma'lumot yozasila va read qilasilar
# 2. 'w' orqali ichiga ota ona haqida inputdan ma'lumot kiritamiz
# 3. 'a' orqali qiziqishilarni qo'shasilar


fayl = open('lesson_23\malumot.txt', 'r+') # read and write
print(fayl.read())
fayl.write("Bu men haqimda ma'lumotlar")
fayl.close

fayl = open('lesson_23\malumot.txt', 'w+') # write and read
fayl.write("Bu men haqimda ma'lumotlar")
print(fayl.read())
fayl.close








