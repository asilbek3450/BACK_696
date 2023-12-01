import random

my_list = []

i = 0
while i < 10:
    my_list.append(random.randint(1, 100))
    i += 1

print(my_list)

new_list = [93, 70, 15, 33, 27, 71, 27, 35, 82, 41]
son = random.choice(new_list)
print(son)
