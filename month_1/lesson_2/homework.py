# - Foydalanuvchidan ikki son kiritishni so'rang. Sonlarni qo'shing, ayirib oling, ko'paytiring va bo'ling.
# Natijalarni konsolga chiqaring.

# - Coffee Shop. Uch turdagi qahva (Amerikano, latte, kapuchino) va uni kutayotgan bitta mijoz yarating. Kofe
# nomlari va narxlarini saqlash uchun o'zgaruvchilardan foydalaning, umumiy narx va mijoz tomonidan buyurtma qilingan
# qahvani ko'rsating.

kofe1 = "Amerikano"
kofe2 = "Latte"
kofe3 = "Kapuchino"

narx1 = 10000
narx2 = 15000
narx3 = 20000

mijoz = input("Ismingizni kiriting: ")

print(f"Assalomu alaykum, {mijoz}! Bizning kofe do'konimizga xush kelibsiz!")
print(f"""Kofe nomlari va narxlari: 
    {kofe1} - {narx1} so'm 
    {kofe2} - {narx2} so'm 
    {kofe3} - {narx3} so'm""")

buyurtma = input("Buyurtma qilmoqchi bo'lgan kofe nomini kiriting: ").title()

if buyurtma == kofe1:
    print(f"{buyurtma}ni narxi {narx1}")

if buyurtma == kofe2:
    print(f"{buyurtma}ni narxi {narx2}")

if buyurtma == kofe3:
    print(f"{buyurtma}ni narxi {narx3}")
