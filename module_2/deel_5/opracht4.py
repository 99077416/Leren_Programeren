from fruitmand2 import fruitmand
from random import randint

aantal = int(input('getal: '))

for i in range(aantal):
    random = randint(1,len(fruitmand)-1)
    fruit = fruitmand[random]
    print(fruit['name'])