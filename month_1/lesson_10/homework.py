# '''Uy ishi

# - while orqali 1 dan 100 gacha 2 va 4 ga birdaniga bo'linadigan sonlar nechtaligini toping
# - while orqali 10 random son yarating (input dan foylanuvchi kiritishi kerak) va ularni har birini yangi listga qo'shib keting.
# - ichida 10 son bor list yarating. While orqali shu list ichidagi faqat juft sonlarni print qiling
# - ichida 10 son bor list yarating. Uni uchida barcha 10 dan katta bo'lgan sonlarni yangi listga olib chiqing
# - Ushbu kodni while orqali yozib bering.

# new_list = []
# for i in range(1, 100):
#     if i % 5 == 0 and i % 2 == 0:
#         new_list.append(i)
# print(mew_list)

# - Ushbu holatda yulduzchalarni print qiling:

# ******
# *****
# ****
# ***
# **
# *

# '''

# # 1
# # i = 1
# # count = 0
# # while i <= 100:   
# #     if i % 2 == 0 and i % 4 == 0:
# #         count = count + 1
# #         print(i)
# #     i = i + 1
# # print(f"2 ga va 4 ga bo'linadigan sonlar {count}ta")


# # 2-topshiriq

# # numbers = []
# # i = 1
# # while i <= 10:
# #     numbers.append(input("Istalgan sonni kiriting: "))
# #     i += 1
# # print(numbers)

# new_list = []
# for i in range(1, 101):
#     if i % 5 == 0 and i % 2 == 0:
#         new_list.append(i)
# print(new_list)
# # 3-topshiriq

# numbers = [5, 1, 8, 10, 2, 7, 3, 21, 91, 13, 45678] #11

# i = 0
#         # 11
# while i < len(numbers): 
#     if numbers[i] % 2 == 0:
#         print(numbers[i])
#     i += 1

# # - ichida 10 son bor list yarating. Uni uchida barcha 10 dan 
# # katta bo'lgan sonlarni yangi listga olib chiqing

numbers = [5, 1, 8, 10, 2, 7, 3, 21, 91, 13]
new_numbers = []
i = 0
while i < len(numbers):
    if numbers[i] > 10:
        new_numbers.append(numbers[i])
    i += 1
print(new_numbers)
