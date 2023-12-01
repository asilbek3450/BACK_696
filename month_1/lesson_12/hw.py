import random

player1 = 0
player2 = 0

while True:
    play1 = random.randint(1, 6)
    play2 = random.randint(1, 6)
    print(f"1-o'yinchi {play1}")
    print(f"2-o'yinchi {play2}")

    if play1 > play2:
        player1 += 1
        print(f"Player1 WON: {play1}")
    elif play1 < play2:
        player2 += 1
        print(F"Player2 WON: {play2}")
    else:
        print("It's TIE")

    con_or_brk = input("Yana o'ynashni istaysizmi?(Yes or NO): ").title()
    if con_or_brk == "Yes":
        continue
    elif con_or_brk == "No":
        break
    else:
        print("Noto'g'ri buyruq!")
        break

print(f"Player1 ning umumiy bali: {player1}")
print(f"Player2 ning umumiy bali: {player2}")