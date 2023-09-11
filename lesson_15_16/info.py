# dict nima
"""
ordered or unordered
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
does not allow duplicates
changeable (mutable)
indexed
can be nested
can be created by using the built-in dict() function

Lug'atlar ma'lumotlar qiymatlarini kalit: qiymat juftlarida saqlash uchun ishlatiladi.
Lug'atlar jingalak qavslar bilan yozilgan bo'lib, kalit va qiymatlarga ega:
"""

# Python Dictionaries
# Access Items
# Change Items
# Add Items
# Remove Items
# Loop Dictionaries
# Copy Dictionaries
# Nested Dictionaries
# Dictionary Methods
# - clear()
# - copy()
# - fromkeys()
# - get()
# - items()
# - keys()
# - pop()
# - popitem()
# - setdefault()
# - update()
# - values()
# Dictionary Exercise

odam = {'name': "Asilbek", 'age': 23, 'weight': 90, 'cars': ['Matiz', 'Nexia', 'BYD']}
# print(odam.keys())  # keylarini chiqarib beradi
# print(odam.values())
# print(odam['cars'])

# change
print(odam)
odam.update(age=25, cars='Malibu')  # 2-usul
print(odam)

# add
odam['height'] = 180  # 1-usul
print(odam)
odam.update(familiya='Mirolimov')  # 2-usul
print(odam)

# remove qilish
# odam.pop('age')
# print(odam)
# odam.popitem()
# print(odam)
# del odam['cars']
# print(odam)


# Loop
print(odam.items())  # hamma elementlarini olish uchun
for i in odam.items():
    print(i)
for i in odam.values():
    print(i)
for i, j in odam.items():
    print(f'{i} degan keyda {j} value bor')


family = {
    'ota': {
        'ismi': 'a',
        'yoshi': 40,

    },
    'ona': {
        'ismi': 'b',
        'yoshi': 35,
    },
    'bola': {
        'ismi': 'c',
        'yoshi': 15,
    }
}
print(f"Otasini yoshi {family['ota']['yoshi']}")
