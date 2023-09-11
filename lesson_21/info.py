
def add_element(sonlar: list, yangi_son):
    return sonlar.append(yangi_son)


juftlar = [4, 8, 2]
print(juftlar)
add_element(juftlar, 1111111111)
print(juftlar)

# lambda function
# lambda function - bu funksiya nomi yo'q, bir qatorlik funksiya

# avzalliklari:
# 1. bir qatorlik funksiya

# 2. return qilish shart emas

# 3. parametr sifatida *args va **kwargs qabul qilishi mumkin

# 4. lambda funksiyalarda if, else, elif operatorlari ishlatilmaydi

# 5. lambda funksiyalarda list comprehension ishlatilishi mumkin
#    list comprehension - bu listni qisqacha yaratish usuli. Misol uchun: mylist = [i for i in range(10)]

# 6. lambda funksiyalarda map, filter, reduce funksiyalari ishlatilishi mumkin


# a, b, c = 10, 50, 20
# # lambda args: code of function
# result = lambda son1, son2, son3: son1 * son2 * son3
# print(result(a, b, c))
#
# name = 'Isfandiyor'
# age = 10
# doc = lambda a, b: print(f"{a}ni yoshi {b}")
# doc(name, age)
#
