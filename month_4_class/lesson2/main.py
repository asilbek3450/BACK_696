products = {
    'airpods': 559,
    'keyboard': 350,
    'powerbank': 559,
    'watch': 759,
    'kb_stick': 29,
    'mphone': 3349,
    'earphones': 459,
    'mini': 20,
    'sticker': 50,
    'notebook': 200
}


class Student:  # student of Mars IT school
    def __init__(self, name, surname, age, course, coins):
        self.name = name
        self.surname = surname
        self.age = age
        self.course = course
        self.coins = coins

    def get_info(self):
        return (f'{self.name} {self.surname} o\'quvchining yoshi {self.age} da, '
                f'{self.course} kursida o\'qiydi, {self.coins} ta coinlari bor')

    def buy_product(self):
        print(f'{self.name}da {self.coins} coins bor')
        info = ""
        for pr, c in products.items():
            info += f'Sizni {pr} sotib olishingiz uchun coin yetadi' if c <= self.coins else f'Sizga {pr} sotib olish uchun {c - self.coins} yetmayapti'
            info += '\n'
        return info


student1 = Student('Toxir', 'Erkinov', 8, 'pro', 1)
student2 = Student('Kamron', 'Unkindiyev', 11, 'pro', 2)
student3 = Student('Zubayr', 'Krisayev', 10, 'pro', 15000)
student4 = Student('Adham', 'Aqltoyev', 12, 'pro', 150)
student5 = Student('Umar', 'Dangasaev', 11, 'pro', 6)
Kutubxona = [book1, ]
# for orqali kiritilgan studentni qaysi mahsulotlarni sotib olishi mumkin ekanligini topish kerak
qr = input("Qaysi student uchun mahsulotlar (1,2,3,4,5): ")
if qr == '1':
    print(student1.buy_product())
