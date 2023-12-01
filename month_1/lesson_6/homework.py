
"""
1. number = "112233" ushbu string formatdagi raqamni ikkichi va oxirgi o'rindagi raqamlarini yig'indisini toping
2. Odamdan string formatda text so'rang agar usha so'zni ichida ikkita unli harf bor bo'lsa "Hello" chiqsin
    agar udan oz bo'lsa "Hayr" chiqsin.
3. for orqali 1-200 gacha 7 va 9 va 11 ga bo'linadigan sonlarni print qiling
4. for va range orqali 1-100 gacha 3 va 5 ga bo'linadigan sonlar nechta ekanligini toping
"""


# 3-topshiriq

for num in range(1, 2000):
    if num % 7 == 0 and num % 9 == 0 and num % 11 == 0:  # Birdan 200 gacha 7 ga, 9 ga va 11 ga bo'linadigan sonlar mavjud emas!!!
        print(num)

print('salom'[0:1])