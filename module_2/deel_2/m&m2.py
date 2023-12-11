from random import choice

kleuren = ('rood','blauw','groen','geel','bruin')

aantal = int(input("hoeveel M&M's?: "))


zak_mnm = {}
zak_mnm['oranje'] = 0

for i in range(aantal):
    kleur = choice(kleuren)
    if kleur in zak_mnm:
        zak_mnm[kleur] += 1
        zak_mnm['oranje'] += 1
    else:
        zak_mnm[kleur] = 1

print(zak_mnm)
