# Inkapsulatsiya

class Auto:

    def __init__(self, name, brand, color, speed, km, country, price):
        self.name = name
        self.brand = brand
        self.color = color
        self.__speed = speed  # private
        self.km = km
        self.country = country
        self.price = price

    def get_auto_speed(self):
        return f'{self.__speed} tezlikka chiqa oladi'

    def get_auto_info(self):
        text = (f'{self.name} rusumli avtomobil, {self.brand} brandi ostida {self.country} da ishlab chiqarilgan, '
                f'{self.color} rangli, maksimal tezligi {self.__speed}')
        return text

    def get_km(self):
        return f'{self.km} km masofa yurgan !'

    def add_km(self, masofa):
        if masofa > 0:
            self.km += masofa
        else:
            print('Km ni kamaytirish mumkin emas')


auto1 = Auto('spark', 'GM', 'oq', 180, 100000, 'Uzb', '9000 $')
auto2 = Auto('gentra', 'GM', 'qora', 210, 10000, 'Uzb', '14000 $')
auto3 = Auto('malibu', 'GM', 'qizil', 230, 5000, 'Uzb', '25000 $')

auto2.add_km(-1000)
auto3.__speed = 250
print(auto2.get_km())
print(auto3.get_auto_speed())
