# Funksiya nima? | return | parameter

# return - funksiyadan qiymat qaytarish uchun ishlatiladi.
# return bo'lmagan funksiyalarda None qaytariladi (NoneType).
#

# 1. Funksiyalarga parametrlar yozish
# 2. Funksiyalarga argumentlar yozish
# 3. Funksiyalarga return yozish
# 4. Funksiyalarga *args va **kwargs yozish



# bo'sh list yarating va unga 10 ta random son qo'shib beradigan funksiya yarating
import random
numbers = list()
def random_sonlar(mylist: list):
    for i in range(10):
        son = random.randint(1, 100)
        mylist.append(son)
    print(mylist)

random_sonlar(numbers)












