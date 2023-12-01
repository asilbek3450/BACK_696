
# i = 1
# while i <= 10:
#     print(i, "I love you")
#     i = i + 1

# while orqali 1 dan 100 gacha toq sonlarni ekranga chiqaring:
# i = 1
# while i <= 100:
#     if i % 2 == 1:
#         print(i)
#     i = i + 1

# while orqali 1 dan 100 gacha 3 ga va 5 ga bo'linadigan
# sonlarni ekranga chiqaring:

# i = 1
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1  # i = i + 1


# while orqali 100 dan 1 gacha juft sonlarni ekranga chiqaring:

i = 100 
while i >= 1:
    i -= 1
    if i == 50:
        break
    elif i % 10 == 0:
        continue
    elif i % 2 == 0:
        print(i)


