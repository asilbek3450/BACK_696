cards = {
    "user1":
        {
            "card_number": '1234567812345678',
            "pin_code": "7777",
            "full_name": "Asilbek Mirolimov",
            "balans": 5000000,
            "duration": "0126",
        },

    "user2":
        {
            "card_number": '1234123412341234',
            "pin_code": "1111",
            "full_name": "Falonchi Pistonchiev",
            "balans": 50000000000,
            "duration": "0528",
        },
}

user_card = input("Karta raqam kiriting: ")
user_pin = input("PIN code kiriting: ")

for key, value in cards.items():
    # print(key, value)
    if value["card_number"] == user_card and value["pin_code"] == user_pin:
        print(f"Welcome {value['full_name']}")
        choice = input("""
    1. balans
    2. paynet
    3. kartadan kartaga
    4. pul yechish
Tanlovingizni kiriting: """)

        if choice == '1':
            print(f"Sizning hisobingizda {value['balans']}")
        elif choice == '2':
            phone_number = input("Qaysi raqamga pul tashlash kerak: ")
            summa = int(input("Qancha: "))
            value['balans'] -= summa
            print(f"Sizni hisobingizdan {summa} yechib olindi\nQoldiq: {value['balans']}")
