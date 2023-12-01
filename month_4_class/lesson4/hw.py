
class Fruit:
    def __init__(self, color, taste, price):
        self.color = color
        self.taste = taste
        self.price = price

    def get_info(self):
        return f"{self.color} rangli, {self.taste} ta'mli, {self.price} so'mlik meva"

    def get_price(self):
        return f"{self.price} so'm"

    def set_price(self, new_price):
        self.price = new_price

    def get_color(self):
        return f"{self.color} rangli"


class Apple(Fruit):
    def __init__(self, color, taste, price, size):
        super().__init__(color, taste, price)
        self.size = size

    def get_info(self):
        return f"{self.color} rangli, {self.taste} ta'mli, {self.price} so'mlik, {self.size} o'lchamli olma"

    def get_size(self):
        return f"{self.size} o'lchamli"


class Banana(Fruit):
    def __init__(self, color, taste, price, numbers):
        super().__init__(color, taste, price)
        self.numbers = numbers

    def get_info(self):
        return f"{self.color} rangli, {self.taste} ta'mli, {self.price} so'mlik, {self.numbers} ta banan"


