class Avto:
    def __init__(self, name, model, color, year, price):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.name} {self.model}"

    def __getitem__(self, item):  # for dict
        return self.__dict__[item]

    def __setitem__(self, key, value):  # for dict
        self.__dict__[key] = value

    def __delitem__(self, key):  # for dict
        del self.__dict__[key]

    def __call__(self, *args, **kwargs):  # for function
        print(f"Bu call metod ishladi, ya'ni obyekt chaqirilganda ishlaydi {self.model}")


obj1 = Avto('BMW', 'X5', 'black', 2015, 75000)
obj2 = Avto('Mercedes', 'S500', 'white', 2018, 90000)

# __getitem__ uchun
print(obj1.__dict__)
print(obj1['name'])
print(obj1['model'])

# __setitem__ uchun
obj1['name'] = 'Audi'
print(obj1['name'])
print(obj1)
del obj1['name']
print(obj1.__dict__)

# __call__ uchun
obj1()
obj2()








# Avtosalon va Avtomobil degan class va tegishli attributlari yaratiladi.
# - Avtosalonga avtomobillar obyektini ro'yxatini saqlash uchun list yaratiladi.
# - Avtosalon classga avtomobillar ro'yxatini qo'shish uchun add_car(), ko'rish uchun show_cars() metodini yaratiladi.
# - dunder metod yordamida avtosalonga avtomobil qo'shish yoki ayirish mumkin bo'lsin,
#   misol uchun:
#   gm degan avtosalon bor va matiz degan avtomobil bor.
#   print(gm+matiz) desak qo'shib bersin, print(gm-matiz) desak olib tashlasin
