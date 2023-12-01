# import requests
#
# my_url = 'https://nbu.uz/uz/exchange-rates/json/'
# data = requests.get(url=my_url)
#
# for i in data.json():
#     if i['code'] == 'USD':
#         print(f'1 $ = {i["cb_price"]} so\'mga teng')


import requests

my_url = 'https://hp-api.onrender.com/api/characters'
data = requests.get(url=my_url)
all_characters = {}

for i in data.json():
    all_characters[i['name']] = """
Name: {}
Actor name: {}
House: {}
Birth day: {}
image: {}
""".format(i['name'], i['actor'], i['house'], i['dateOfBirth'], i['image'])

print(all_characters['Harry Potter'])
