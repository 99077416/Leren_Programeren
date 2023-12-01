from random import randint

kleuren = ('oranje', 'blauw', 'groen', 'bruin')

aantal = int(input("hoeveel M&M's?: "))

zak = []

for i in range(aantal):
    zak.append(kleuren[randint(0,3)])

print(zak)
