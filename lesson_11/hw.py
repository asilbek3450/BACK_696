

while True:
        
    number1 = int(input('1son yozing: '))

    number2 = int(input('2son yozing: '))

    operator = input("operatorni kirititing(+,-,*,/,//,%) ")

    if operator == '+':
        print(number1 + number2)

    if operator == '-':
        print(number1 - number2)

    if operator == '*':
        print(number1 * number2)

    if operator == '/':
        print(number1 / number2)

    if operator == '//':
        print(number1 / number2)

    if operator == '%':
        print(number1 % number2)
    
    davomettirish = input('davom etasizmi: ')
    if davomettirish == 'yoq':
        break
    if davomettirish == 'ha':
        continue