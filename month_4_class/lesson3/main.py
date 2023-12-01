# Uyga vazifa
# Konstruktorlar (amaliyot)
class Avto:
    # get_km, add_km, get_narh, set_narh, get_model, set_model, get_make

    def __init__(self, make, model, rang, yil, narh):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.kilometr = 0

    def get_info(self):
        return (f"{self.rang} {self.make} {self.model}. "
                f"Narhi: {self.narh}. Yili: {self.yil}. Bosib o'tgan km: {self.kilometr}")

    def get_narh(self):
        return f'{self.narh} $'

    def set_narh(self, yangi_narh):
        self.narh = yangi_narh


# 5 ta avtomobil obyektini yaratish

avto1 = Avto('GM', 'Matiz', 'oq', 2010, 4000)
print(avto1.get_info())
print(avto1.model)
print(avto1.narh)
print(avto1.get_narh())
avto1.set_narh(5000)
print(avto1.get_narh())
