# 1. Klaviaturadan ikkita son kiriting. Ushbu sonlar kvadratlari summasi kattami yoki summasining kvadrati kattami
# aniqlang. Javobni habar ko`rinishida ekranga chiqaring.

a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))

# (**) - darajasini topadi: 5 ni 2 chi darajasini chiqarish uchun: print(5 ** 3) => 5*5*5

x = a ** 2 + b ** 2
y = (a + b) ** 2

if x > y:
    print(f"kvadratlari summasi katta {x} > {y}")
elif x < y:
    print(f"summasining kvadrati {y} > {x}")
else:
    print(f"IKkalasi teng {x} = {y}")





# 2. Staj uchun qo'shiladigan qo`shimcha haqni hisoblang, agar staj 2 dan 5 yilgacha bo`lsa 2%, agar 5 dan 10
# yilgacha bo`lsa 5% ustama qo`shiladi. Klaviaturadan oylik va stajni kiriting, ustama va umumiy oylikni chiqaring.

