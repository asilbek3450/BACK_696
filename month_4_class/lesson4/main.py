# Inheritence and Polymorphism (Vorislik va Polimorfizm)

# Vorislik - bir classning boshqa classdan xususiyatlarini o'zlashtirish
# Polimorfizm - voris classning metodlarini o'zgartirish

class Person:  # super class

    def __init__(self, ism, familiya, yoshi, manzil):
        self.ism = ism
        self.familiya = familiya
        self.yoshi = yoshi
        self.manzil = manzil

    def get_info(self):
        return f"{self.ism} {self.familiya}, yoshi {self.yoshi}. {self.manzil}da yashaydi"


class Student(Person):  # meros qilib olish
    def __init__(self, ism, familiya, yoshi, manzil, kasbi):
        super().__init__(ism, familiya, yoshi, manzil)
        self.kasbi = kasbi

    def get_info(self):  # polimorfizm (metodni ishlashi o'zgartiriladi)
        return f"{self.ism} {self.familiya}, yoshi {self.yoshi}. {self.manzil.get_manzil()}, {self.kasbi} bo'lib ishlaydi"


student1 = Student('Umar', 'Hamidjonov', '9', 'Ko\'kcha', "quruvchi")

# print(student1.get_info())


# Person class ga t_yil, millati attributlari qo'shish
#                 get_fullname(), get_age(), get_address() metodlarini yaratish
# 2 ta student object yaratish

# Teacher degan Person dan meros class qilinadi
# oylik, fani degan attributlar qo'shiladi,
# get_info() o'zgartiriladi, bunda oyligi va o'tadigan fani haqida ham ma'lumot beriladi


# obyekt ichida obyekt
class Manzil:
    def __init__(self, uy, kocha, tuman, shahar, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.shahar = shahar
        self.viloyat = viloyat

    def get_manzil(self):
        return (f"{self.viloyat} viloyati, {self.shahar} shahri, {self.tuman} tumani, "
                f"{self.kocha} ko'chasi, {self.uy}-uyda yashaydi")


manzil2 = Manzil(12, 'Ko\'kcha', 'Yunusobod', 'Toshkent', 'Toshkent')
print(manzil2.get_manzil())
student2 = Student('Umar', 'Hamidjonov', '9', manzil=manzil2, kasbi="uchuvchi")
print(student2.get_info())
