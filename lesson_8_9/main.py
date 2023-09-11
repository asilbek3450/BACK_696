oquvchilar = ['Usmon', '231', 'Fazliddin', '1234567', 'Doniyor', '11', 'Toxir']

# Add List Items
oquvchilar.append('qwertyuiop')
oquvchilar.insert(3, 'Kamronbek')

# Change List Items
oquvchilar[1] = 'MARS'

print(oquvchilar)
# Remove List Items
# oquvchilar.remove([1, 2, 3])
oquvchilar.pop(6)
# oquvchilar.clear()

# Loop Lists
for i in range(len(oquvchilar)):
    if i % 2 == 0:
        print(oquvchilar[i])

print(oquvchilar)

# # Access List Items
# # print(oquvchilar[0])
# # print(oquvchilar[5])
# # print(oquvchilar[2:5])
#
# # Change List Items
# oquvchilar[0] = 'Umar'
# print(oquvchilar)
#
# # Add List Items
# print(type(oquvchilar))
# oquvchilar.append('Usmon')  # oxiriga qo'shadi
# oquvchilar.insert(5, 'MARS')  # man xoxlagan indexga qo'shadi
# print(oquvchilar)
#
# # Remove List Items
# oquvchilar.remove()  # tanlangan elementni o'chiradi
# oquvchilar.pop()  # tanlangan index bo'yicha o'chiradi, yozilmasa oxiridan o'chiradi
# print(oquvchilar)
#
# # Loop list - sikl
# # for raqam in range(1, 101):
# #     print(raqam)
#
# soni = len(oquvchilar)
# print(soni)
#
#
#
# text = 'fazliddin'
# print(text.islower())
#
#
#
# ichida 10 ta meva bor list yarating, for ochib har bitta mevani if bilan tekshiring,
# agar kichik harfda yozilgan bo'lsa katta harfga o'tqazing, aks holda teskarisi

# mevalar = ['apple', 'lemon', 'Melon', 'bAnana', 'pineapple']
# new = []
# for i in mevalar:
#     if i.islower():
#         new.append(i.upper())
#     else:
#         new.append(i.lower())
#
# print(new)
# shu listda juft index larni hamasini 'mars' degan elementga o'zgatirib qo'yish

