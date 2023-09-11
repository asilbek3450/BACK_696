# Arifmetik operatorlarni takrorlash (+, -, *, /, //, %, **)
# Taqqoslash operatorlari (<, >, <=, >=, ==, !=)

son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
print(type(son1))
print(son1 > son2)
print(son1 < son2)
print(son1 <= son2)
print(son1 >= son2)
print(son1 == son2)
print(son1 != son2)

number1 = int(input('1- '))
number2 = int(input("2- "))
operator = input("Operatorni kiriting(+,-,*,/,//,%): ")

if operator == '+':
    print(number1 + number2)


