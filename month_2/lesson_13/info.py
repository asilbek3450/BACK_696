#
# 1. Odamdan ismini input orqali so'rang. Va uning ichida nechta unli harf borligini topib beradigan kod yozing.
name = input("Ismingizni kiriting: ")
unli = 'aeiou'
count = 0
for i in name.lower():
    if i in unli:
        count += 1
print(f"{name} da {count} ta unli harf bor")

# 2. for va range 1 dan 100 gacha juft sonlarni print qiling.
# 3. Ushbu list ichidagi juft sonlar nechtaligini toping.
#     numbers = [12, 22, 32, 4, 66, 43, 12, 122, 43, 67, 89, 64, 22, 222, 11]
# 4. Odamdan 0 dan katta son bo'lgan son kiritishini so'rang. Va 0 dan boshlab usha songacha bo'lgan sonlarni
#    yig'indisini topadigan kod yozing.
# 5. while orqali 1 dan 1000 gacha bo'lgan toq sonlarni yig'indisini topadigan kod yozing.
#
#
# 6. Userdan input sifatida integer raqam so'raysiz. U manfiy ham bo'lishi mumkin. Vazifangiz uni teskari qilib qaytarish.
#    Masalan: 123 => 321, -12 => -21
# 7. Ushbu list ichidan 3 va 7 ga qoldiqsiz bo'linadigan sonlarning yig'indisni toping.
#     numbers = [12, 22, 21, 4, 66, 43, 42, 122, 43, 67, 84, 64, 22, 222, 11]
# 8. Odamdan input orqali ismini kiritishini so'rang va while orqali ismini har bir harfini birma bir print qiling.
# 9. Odamdan ikki xonali son sorang va usha sonni ikkala sonini bir birga qo'shib bering. Masalan:
#     odam 12 kiritsa unga 3 qaytarasiz chunki 12 -> 1 + 2 = 3
#     odam 54 kiritsa unga 9 qaytarasiz chunki 54 -> 5 + 4 = 9
# 10. Odamdan input orqali text so'rang va uni ichida nechta so'z borlini topib beradigan kod yozing.
