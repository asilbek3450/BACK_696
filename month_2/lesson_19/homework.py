a = int(input('son kiriting: '))
b = int(input('son kiriting: '))
c = int(input('son kiriting: '))

def eng_katta(a,b,c):
    if a > b and a > c: # agar
        print(f"Eng kattasi {a}")
    elif b > a and b > c: # yoki
        print(f'Eng kattasi {b}')
    elif c > a and c > b:
        print(f'Eng kattasi {c}')
    else:
        print("Eng kattasi yoq")
eng_katta(a,b,c)


def yigindi(a,b,c):
    print(a+b+c)
yigindi(a,b,c)

def kopaytma(a,b,c):
    print(a*b*c)
kopaytma(a,b,c)


text = str(input('text kiriting: '))
def teskari(text):
    print(text[::-1])
teskari(text)

x = int(input('son kiriting: '))
y = int(input('son kiriting: '))
def daraja(x,y):
    print(x*y)
daraja(x,y)

son = int(input('son kiriting: '))
def juft_toq(son):
    if son % 2 == 0:
        print('kiritgan soningiz juft')
    elif son % 2 == 1:
        print('kiritgan soningiz toq')
juft_toq(son)