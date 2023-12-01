"""
Uyga Vazifa💻
=> Vazifa: "Mars Shop" dasturini yaratish

Siz ""Mars Shop"" dasturini ishlab chiquvchisiz - Marsdagi oddiy onlayn-do'kon. Sizning vazifangiz asosiy funktsiyalarni sinab ko'rish uchun dasturning soddalashtirilgan versiyasini yaratishdir.

1. “Mahsulot” (Mahsulot) sinfini yarating:
    - mahsulot quyidagi atributlarga ega bo'lishi kerak: mahsulot nomi (nomi) va narxi (narxi).

2. “Shop” sinfini yarating (Shop):
    - Do'konda mahsulotlarni assortimentga qo'shish usuli bo'lishi kerak. Ushbu usul mahsulot nomini va uning narxini olishi va mahsulotni mavjud mahsulotlar ro'yxatiga qo'shishi kerak.

3. “Savat” sinfini yarating (Savat):
    - Aravada narsalarni qo'shish, xaridning umumiy qiymatini hisoblash va savatdagi narsalar haqidagi ma'lumotlarni ko'rsatish usullari bo'lishi kerak.

4. Dastur bilan o'zaro aloqa:
    - Foydalanuvchilarga do'kondagi mavjud narsalarni ko'rish, ularni savatga qo'shish va keyin tanlangan mahsulotlarning umumiy narxini ko'rish imkonini beruvchi oddiy interfeys yarating.

5. Qo'shimcha funktsiyalar (ixtiyoriy):
    - Aravadan narsalarni olib tashlash qobiliyatini amalga oshiring.
    - Xaridni yakunlaydigan va buyurtma ma'lumotlarini ko'rsatadigan ""Checkout"" funksiyasini qo'shing.

Sizning ""Mars Shop"" versiyangiz Marsdagi onlayn-do'konning oddiy va tushunarli namunasiga aylansin, bu foydalanuvchilarga mahsulotlarni savatga qo'shish va xaridning umumiy qiymatini hisoblash jarayonini o'zlashtirishga yordam beradi! Rivojlanishda omad!
Coins:
1.1-talab: Atributlar bilan "Mahsulot" (Mahsulot) sinfini yarating: mahsulot nomi (nomi) va narxi (narxi).-2coins🪙
2.2-talab: Do'konda assortimentga mahsulot qo'shish usuli bo'lishi kerak. Ushbu usul mahsulot nomini va uning narxini olishi va mahsulotni mavjud mahsulotlar ro'yxatiga qo'shishi kerak.-2coins🪙
3.3-talab: Aravada narsalarni qo'shish, xaridning umumiy qiymatini hisoblash va savatdagi narsalar haqidagi ma'lumotlarni ko'rsatish usullari bo'lishi kerak.-4coins🪙
4.4-talab: Foydalanuvchilarga do'kondagi mavjud narsalarni ko'rish, ularni savatga qo'shish va keyin tanlangan mahsulotlarning umumiy narxini ko'rish imkonini beruvchi oddiy interfeys yarating.-4coins🪙

--------------------------------------------------------------------
"""


class Product:

    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

    # def __str__(self):
    #     return f"{self.nomi} - {self.narxi} so'm"

    def __repr__(self):  # representation
        return f"{self.nomi} - {self.narxi} so'm"


class Shop:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        text = 'Do\'konimizdagi mahsulotlar:\n'
        for product in self.products:
            text += f"{product.nomi} - {product.narxi} so'm,\n"
        return text


class Basket:

    def __init__(self, ):
        self.basket = {}

    def add_basket(self, product, quantity):
        self.basket[product] = quantity
        # basket['pen'] = 10, basket['mouse'] = 5

    def check_info(self):
        total_price = 0
        check = ''
        for product, quantity in self.basket.items():
            total_price += product.narxi * quantity
            check += product.nomi + '-' + str(quantity) + 'ta\n'
        return check, total_price


# shop yaratish
mars_shop = Shop()

# mahsulot yaratish
product1 = Product('mishka', 50000)
product2 = Product('klaviatura', 199000)
product3 = Product('sticker', 70000)
product4 = Product('fleshka', 149000)
product5 = Product('telefon', 1490000)
product6 = Product('ruchka', 5000)

all_products = [product1, product2, product3, product4, product5, product6]

# shopga mahsulot qo'shish
mars_shop.add_product(product1)
mars_shop.add_product(product2)
mars_shop.add_product(product3)
mars_shop.add_product(product4)

print("1. Shopdagi mahsulotlarni ko'rish,\n"
      "2. Shopga mahsulot qo'shish,\n"
      "3. Mahsulot yaratish,\n"
      "4. Mahsulotlar sotib olish,\n"
      "5. Chiqish.\n")

while True:
    option = input("MarsShop dasturimizga xush kelibsiz, menyuni tanlang: ")

    if option == '1':
        print(mars_shop.get_products())
    elif option == '2':
        print(all_products)
        user_product = input("Qaysi mahsulotni qo'shish kerak: ")

        if user_product == 'mishka':
            mars_shop.add_product(product1)
        elif user_product == 'klaviatura':
            mars_shop.add_product(product2)
        elif user_product == 'sticker':
            mars_shop.add_product(product3)
        elif user_product == 'fleshka':
            mars_shop.add_product(product4)
        elif user_product == 'telefon':
            mars_shop.add_product(product5)
        elif user_product == 'ruchka':
            mars_shop.add_product(product6)
        else:
            print("Bunday mahsulot yo'q")



        # uyga vazifa 2,3,4,5 menyularni qilish
