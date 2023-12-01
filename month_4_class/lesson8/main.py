# dunder methods, 2nd part


# 1. __getitem__(), __setitem__(), __delitem__()
# 2. __dict__(), __dir__()
# 3. __call__()
# 4. __new__(), __init__()
# 5. __iter__(), __next__()
# 6. __enter__(), __exit__()
# 7. __add__(), __sub__(), __mul__(), __div__()
# 8. __eq__(), __lt__(), __gt__(), __le__(), __ge__()


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
