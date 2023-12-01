print("Welcome to Coffe Shop!!!")
Amer = 8000
Latte = 9000
Kapuch = 8500
print("We have Americano, Latte,Kapuchino")
print("press 1 for Americano(8000som)")
print("press 2 for Latte(9000som)")
print("press 3 for Kapuchino(8500som)")

shtuk = int(input("How many cup of coffee do you want?  "))

choice = int(input("What cofe do you want(Americano, Latte,Kapuchino)?  "))
if choice == 1:
    print("You should pay",Amer,"som for 1 cup")

    narx_A = shtuk * Amer
    print("You should pay: ",narx_A,"som")
elif choice == 2:
    print("You should pay",Latte,"som for 1 cup")
    narx_L = shtuk * Latte
    print("You should pay: ",narx_L,"som")
else:
    print("You should pay",Kapuch,"som for 1 cup")
    narx_k = shtuk * Kapuch
    print("You should pay: ",narx_k,"som")
    