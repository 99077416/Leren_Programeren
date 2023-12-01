from random import randint, choice

kleuren = ('oranje', 'blauw', 'groen', 'bruin')

aantal = int(input("hoeveel M&M's?: "))

zak = []

for i in range(aantal):
    zak.append(choice(kleuren))

print(zak)
