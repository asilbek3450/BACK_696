# Svetofor

color = input("Rangni kiriting: ").title()

if color == 'Qizil':
    print("Stop!")
elif color == 'Sariq':
    print("Tayyorlan")
elif color == 'Yashil':
    print("Go")
else:
    print("Noto'g'ri rang kiritilgan")


# "Polindrome", Palindrom, misol uchun: non, 12321

word = input("So'z kiriting: ")
if word == word[::-1]:
    print("Bu polindrom so'z")
else:
    print("Polindrom emas")


# Foydalanuvchidan uchta son kiriting, musbatlarini kvadratga oshiring,
# manfiylarini kubini toping. 

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > 0:
    a = a ** 2
else:
    a = a ** 3

if b > 0:
    b = b ** 2
else:
    b = b ** 3

if c > 0:
    c = c ** 2
else:
    c = c ** 3

print(a, b, c)


# Foydalanuvchidan uchta son a, b, c uchburchak tomonlarini qiymatini kiriting,  
# uchburchakni perimetrini va yuzini toping

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
p = a + b + c
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5  # Shu formulasi bo'yicha: https://i.ytimg.com/vi/ZEIdCV1lr-4/maxresdefault.jpg
print("Perimetr: ", p)
print("Yuzasi: ", s)
