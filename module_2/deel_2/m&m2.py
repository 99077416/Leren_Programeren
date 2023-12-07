from random import choice

kleuren = ('rood','blauw','groen','geel','bruin')

aantal = int(input("hoeveel M&M's?: "))


zak_mnm = {}


for i in range(aantal):
    kleur = choice(kleuren)
    if kleur in zak_mnm:
        zak_mnm[kleur] += 1
    else:
        zak_mnm[kleur] = 1

print(zak_mnm)