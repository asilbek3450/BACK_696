# 1-topshiriq

# numbers = (15, 30, 10, 5, 40, 20)
# max_son = max(numbers)
# min_son = min(numbers)
#
# print(max_son)
# print(min_son)

# 2-topshiriq

# my_tuple = (1, "hello", 3.14, False)
# print(my_tuple)
# my_list = list(my_tuple)
#
# my_list[1] = "world"
# my_tuple = tuple(my_list)
# print(my_tuple)

# 3-topshiriq

"""
Tuple oddiy qavs bilan yoziladi(), set esa figurali qavs bilan{}.
Setning ishida ikkita yoki undan ko'p bir hil narsa qatnashgan bo'lmaydi agar shunday kiritilsa ham bir hil qatnashgan narsalarni
faqat birinchisini olib qolib qolganini o'chirib yuboradi.
Tuple ga index orqali murojaat qilish mumkin set ga esa yo'q.
Set ni ichidagi ma'lumotga o'zgartirish kiritish mumkin, Tuple ni o'zgartirib bo'lmaydi.

"""
# 4-topshiriq

my_set = {True, 'mars', 1, 'bir narsa', 2, 3, "salom"}

set_list = list(my_set)

for i in set_list:
    if str(i).isdigit():
        print(i)


# 5-topshiriq

week_list = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
choose = input("Bitta hafta kuni nomini yozing: ").title()

if week_list.index(choose) % 2 == 0:
    print("Bu hafta kuni toq.")
else:
    print("Bu hafta kuni juft.")

# 6-topshiriq

names = set()

# while True:
#     add_name = input("Ism kiriting: ").title()
#     if add_name in names:
#         print("Bu ism avval qatnashgan!")
#     else:
#         names.add(add_name)
#         print("Ism qo'shildi")
#     con_or_brk = input("Yana ism qo'shasizmi? (Y/N): ").title()
#     if con_or_brk == "Y":
#         continue
#     elif con_or_brk == "N":
#         break
#     else:
#         print("Noto'g'ri buyruq!")
#         break
# print(names)