# 1 topshiriq

cars = ("cobalt", "lacetti", "nexia", "spark", "gentra")

if "lacetti" in cars:
    print("lacetti list ichida bor")
else:
    print("lacetti list ichida yoq")

# 2 topshiriq

cars = ("cobalt", "lacetti", "nexia", "spark", "gentra")

if "bmw" in cars:
    print("bmw list ichida bor")
else:
    print("bmw list ichida yoq")

# 3 topshiriq

cars = ("cobalt", "lacetti", "nexia", "spark", "gentra")

print(cars[3])

# 4 topshiriq

cars = ("cobalt", "lacetti", "nexia", "spark", "gentra")

print(cars[2])

# 5 topshiriq

cars = ("cobalt", "lacetti", "nexia", "spark", "gentra")

print(cars[-1])





# qoshimcha

uzavto = ("nexia", "spark", "gentra")
bmw = ("bmw m5", "bmw i7", "bmw x5")

united = uzavto + bmw

united = list(united)

united.pop(2)
united.insert(2, "tayota")

print(united)