# 2. Odamdan qaysi oyda tugilganini input sifatida sorang. Va barcha oylarni
#     malumot sifatida saqlab usha oydan oldingi va keyingi oyni topib bering.

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

month = input("Enter your birth month: ").lower()

month_index = months.index(month)

if month == 'december':
    next_month = months[0]
else:
    next_month = months[month_index+1]
prv_month = months[month_index-1]

print(prv_month, next_month)
