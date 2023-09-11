# Funksiya, dict va shartli ""if"" iborasi:
#
# Mahsulot nomi-miqdori juftlarini o'z ichiga olgan lug'at yarating (masalan, ""olma"": 5, ""banan"": 3 va boshqalar).
# Foydalanuvchidan mahsulot nomini kiritishini so'rang.
# Funksiya yarating va shartli if dan foydalanib, lug'atda shunday mahsulot mavjudligini tekshiring.
# Agar mahsulot lug'atda bo'lsa, uning miqdori haqida xabarni agar mahsulot lug'atda bo'lmasa, uning yo'qligi haqida xabarni qaytaring.
#
# meva-rang juftlarini o'z ichiga olgan lug'at yarating (masalan, ""olma"": ""qizil"", ""banan"": ""sariq"" va
# boshqalar). Foydalanuvchidan meva nomini kiritishni so'rang. Funksiya yarating va if shartli operatorlardan foydalanib,
# berilgan meva rangini tekshiring. Meva rangi haqida tegishli xabarni ko'rsatish (masalan, """"Bu qizil olma""""
# yoki ""Bu meva noma'lum rangda""""). “for” siklida lug‘at va shartli “if” iborasini ko‘rsatish:
#
# Bir nechta turli filmlardan “film nomi-reyting” juftliklarini (masalan, “Forrest Gump”: 8.8, “Yulduzli urushlar”:
# 8.7 va boshqalar) oʻz ichiga olgan lugʻat yarating. Funksiya yarating va “For” tsiklidan foydalanib, har bir filmni aylantiring va uning
# reytingi 8,5 dan yuqori ekanligini tekshiring. Agar filmning reytingi 8,5 dan yuqori bo'lsa, uning yuqori reytingi
# haqida xabarni ko'rsating. Agar filmning reytingi 8,5 dan kam yoki unga teng bo'lsa, uning normal reytingi haqida
# xabarni ko'rsating.

# 2

products = {
    'apple': 'red',
    'banana': 'yellow',
    'pineapple': 'orange',
    'cherry': 'red',
    'orange': 'orange'
}

product_name = input("meva nomini kiriting: ")

def rang_top(nom):
    if nom in products.keys():
        print(f'{nom} ni rangi {products[nom]}')
    else:
        print("Bunday meva yo'q")
rang_top(product_name)



# 3

# movies = {
#     "Interstellar": 6,
#     "The Lord of the Rings": 7,
#     "Fight Club": 8,
#     "Back to the Future": 8
# }

# for i, j in movies.items():
#     if movies[j] > 8:
#         print(i)
