# dunder methods ( __name__() )

# __str__ --> str()
# repr --> repr()
# len --> len()
# add , sub, mul,  --> +, -, *, /
# eq --> ==
# lt, gt, le, ge --> <, >, <=, >=
# lower than, greater than, lower equally, greater equally

# getitem --> []
# setitem --> []
import datetime


class Avto:
    def __init__(self, name, model, color, year, price):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    # def __str__(self):
    #     return f"{self.name} {self.model}"

    def __repr__(self):
        return f"{self.name} {self.model}"

    def __len__(self):  # len() uchun
        return 2023 - self.year

    def __add__(self, other):
        return self.price + other

    def __sub__(self, other):
        return self.price - other

    # __mul__(), __div__

    def __eq__(self, other):
        return self.name == other


obj1 = Avto('BMW', 'X5', 'black', 2015, 75000)
obj2 = Avto('Mercedes', 'S500', 'white', 2018, 90000)

print(len(obj1))
print(len(obj2))

print(obj1 - 1000)
print(obj2 + 5000)

print(obj1 == 'BMW')


# Uyga vazifa:
# 10 ta obyekt qilib yaratish, __getitem__(), __setitem__(), __del__(), __dict()__, __dir__()
# ni nima ish qilishini o'rganish

