from random import shuffle
namen = []
lootjes = {}
toevoegen = 'ja'
while toevoegen == 'ja':
    naam = input('naam: ')
    if naam not in namen:
        namen.append(naam)
    if len(namen) >= 3:
        toevoegen = input('nog een naam toevoegen?')

shuffle(namen)

for i in range(0,len(namen)):
    if i == len(namen)-1:
        lootjes[namen[i]] = namen[0]
    else:
        lootjes[namen[i]] = namen[i+1]


for i in lootjes:
    print(f'{i} {lootjes[i]}')
