class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products = {}  # Mahsulotlar lug'ati

    def get_products(self):
        # Do'konimizdagi mahsulotlar ro'yxatini qaytaradi
        return self.products

    def add_product(self, product_name, price):
        # Yangi mahsulotni lug'atga qo'shish
        self.products[product_name] = price

    def remove_product(self, product_name):
        # Mahsulotni lug'atdan o'chirish
        if product_name in self.products:
            del self.products[product_name]
        else:
            print(f"{product_name} mahsuloti topilmadi")

    def sell_product(self, product_name, quantity):
        # Mahsulotni sotish
        if product_name in self.products and quantity > 0:
            if self.products[product_name] * quantity <= sum(self.products.values()):
                self.products[product_name] -= quantity
                print(f"{quantity} ta {product_name} sotildi. Jami {self.products[product_name] * quantity} so'm")
            else:
                print(f"Do'konimizda yetarli miqdorda {product_name} yo'q")
        else:
            print(f"{product_name} mahsuloti topilmadi yoki miqdor xato")


def main():
    # Do'kon yaratish
    my_store = Store("Moy Do'kon", "Toshkent shahri, Yunusobod tumani")

    while True:
        print("\nDo'konimiz bilan ishlash:")
        print("1. Yangi mahsulot qo'shish")
        print("2. Mahsulotni olib tashlash")
        print("3. Mahsulotni sotish")
        print("4. Do'konni tark etish")
        print("5. Chiqish")

        try:
            print(my_store.get_products())
            option = int(input("Tanlangan amalni kiriting: "))
            if option == 1:
                product_name = input("Yangi mahsulot nomini kiriting: ")
                price = float(input("Mahsulot narxini kiriting: "))
                my_store.add_product(product_name, price)
            elif option == 2:
                product_name = input("Olib tashlashni istagan mahsulot nomini kiriting: ")
                my_store.remove_product(product_name)
            elif option == 3:
                product_name = input("Sotmoqchi bo'lgan mahsulot nomini kiriting: ")
                quantity = int(input(f"Qancha {product_name} sotmoqchisiz? "))
                my_store.sell_product(product_name, quantity)
            elif option == 4:
                break
            elif option == 5:
                print("Dastur tugadi. Xayr!")
                break
            else:
                print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")
        except ValueError:
            print("Noto'g'ri format. Butun son kiriting.")


if __name__ == "__main__":
    main()
