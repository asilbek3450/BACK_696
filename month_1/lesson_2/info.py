"""

- O'tilgan mavzu bo'yicha savollar javob
- Matematik operatorlar haqida ma'lumot
- (+, -, /, *, **, %, //, **) dan foydalanish va misollar
- str (lower, upper, title, capitalize, replace, find, index, count, format,
- isdigit, isalpha, islower, isupper, isspace, isalnum, split, rsplit, lsplit, endswith, startswith,
- str ni kesish va ularni nusxalash usullari
- Matematik va str usullari bilan ishlash
- Pythonda turlarni qanday aylantirishni tushuntirish (casting): int(), float(), str()

"""
# print(5 // 2)
# # (+, -, /, *, **, %, //)

# print(2 ** 4) # 2*2*2*2
# print(9 % 2) # qoldig'ini topib beradi
# print(8 // 3) # butun son qilib bo'lib beradi


# (+, -, /, *, **, %, //)
# o'zgaruvchi yaratib foydalanuvchidan so'rash kerak
# int
# float
# str
number_1 = int(input("1-sonni kiriting: "))
number_2 = int(input("2-sonni kiriting: "))
print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2)
print(number_1 ** number_2)
print(number_1 // number_2)

# son = 6.1
# print(type(son))


# string methods

text = "men IT school o'quvchisiman"
#       012345678910...
# print(text.upper()) # hamma harflarni katta qilib qaytaradi
# lower, 
# title, 
# capitalize, 
# replace, 
print(text.replace("IT", "")) # almashtirish
# find,
print(text.find('i'))
# index, 
# print(text.index('M'))
# count,
print(text.count('o'))
# format, 
print(f"text: {text}")
print(text.format("Mars", '!'))

# isdigit, 
# isalpha
