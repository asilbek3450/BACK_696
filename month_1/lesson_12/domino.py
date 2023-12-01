"""
Uyga vazifa:

Dice Roll (domino)

- 2 ta foydalanuvchi yaratasilar.
 - while ni ichida ikkalasi navbat bilan shunaqa domino tashlaydi, bu random orqali qilinadi (ya'ni 1dan 6gacha random tushadi).
- qaysi foydalanuvchiniki kattaroq tushgan bo'lsa shu yutadi
- while qaytarilishi uchun oldingi vazifadagidek "yana o'ynaysizlarmi" deb so'raydi va unga ha yoki yo'q deb kiritishi kerak: "ha" desa while davom etadi, "yo'q" desa to'xtaydi
- oxirida "yo'q" deb tugatgandan keyin har bitta foydalanuvchi nechi marta yutganini chiqarib berish kerak
"""

import random


user1 = input("1-foydalanuvchi ismini kiriting: ")
user2 = input("2-foydalanuvchi ismini kiriting: ")

user1_win = 0
user2_win = 0

while True:
    user1_dice = random.randint(1, 6)
    user2_dice = random.randint(1, 6)
    print(f"{user1} ga {user1_dice} tushdi")
    print(f"{user2} ga {user2_dice} tushdi")
    if user1_dice > user2_dice:
        user1_win += 1
        print(f"{user1} yutdi 🥳\n")
    elif user2_dice > user1_dice:
        user2_win += 1
        print(f"{user2} yutdi 🥳\n")
    else:
        print("Durrang")
    answer = input("Yana o'ynaysizmi? (ha/yo'q): ")
    if answer == "yo'q":
        break

print(f"\n{user1} {user1_win} marta yutdi")
print(f"{user2} {user2_win} marta yutdi")

print(f"\n{user1} yutdi 😤" if user1_win > user2_win else f"\n{user2} yutdi 😤")


