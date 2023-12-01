# 1. ichida 10 ta son bor list yarating va ularni faqat toqlarini print qiling
# 2. ichida 10 ta son bor list yarating va ularni faqat juftlarini print qiling
# 3. ichida 10 ta son bor list yarating va ularni teskari tartibda print qiling
# 4. bo'sh list yarating, range orqali 1 dan 100 gacha bo'lgan sonlarni ichidan 3 ga va 5 ga bo'linadiganlarini shu listga qo'shing
# 5. guruhdagi hamma bolani ismi bor bo'lgan list yarating, u listni uzunligini toping va o'zingiz yoqtirmagan ismingizni uni ichidan olib tashlang
# 6. guruhdagi bolalar listiga o'zingiz yoqtirgan biror qizni ismini listni oxiriga qo'shing
# 7. guruhdagi bolalar listiga o'zingiz yoqtirgan biror qizni ismini o'zingizni ismingizdan oldingi indexga qo'shing

# 1
my_list = [6, 2, 71, 12, 9, 10, 23, 123, 0, 1]

for i in my_list:
    if i % 2 != 0:
        print(i)

# 2
for i in my_list:
    if i % 2 == 0:
        print(i)

# 3
print(my_list[::-1])

# 4
numbers = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        numbers.append(i)
print(numbers)


# Topshiriqlar
#
# numbers = [12, 11, 23, 1, 23, 43, 5, 67, 65, 23, 43, 22]
#
# 1. Ushbu list ichidagi toq sonlar yig'indisini toping.
# 2. 4-index va 6-indexda turgan sonlar ko'paytmasini toping.
# 3. Ushbu list ichidagi eng kichik raqamni toping.
# 4. Ushbu list ichidagi 2 va 4 ga bo'linadigan sonlarni print qiling.
# 5. Ushbu list ichidagi toq sonlar sonini toping.



hayvon1 = 'ayiq'
hayvon2 = 'sher'

x = input("Qaysi hayvonni kiritasiz: ")

if x == '1':
    print(hayvon1)
    hayvon1_turi = input("Turini kiriting: ")
    hayvon1_vazni = input("Vaznini kiriting: ")
    hayvon1_rangi = input("Rangini kiriting: ")
    hayvon1_yoshi = input("Yoshini kiriting: ")
elif x == '2':
    print(hayvon2)
    hayvon2_turi = input("Turini kiriting: ")
    hayvon2_vazni = input("Vaznini kiriting: ")
    hayvon2_rangi = input("Rangini kiriting: ")
    hayvon2_yoshi = input("Yoshini kiriting: ")

user = input("Qaysi hayvon haqida ma'lumot kerak: ")
if user == '1':
    print(f"Hayvon: Arslon, Og'irligi: 200 kg, Rangi: Sariq, Yoshi: 5 yil, Ismi: Simba")