from fruitmand2 import fruitmand
from random import choice

aantal = int(input('getal: '))


for i in range(aantal):
    print(choice(fruitmand)['name'])