from random import shuffle
namen = []
lootjes = {}
cadeautjes = {}
toevoegen = 'ja'
while toevoegen == 'ja':
    naam = input('naam: ')
    if naam not in namen:
        namen.append(naam)
    cadeau_list = []
    print('voer 3 cadeautjes in die jij graag zou willen krijgen.')
    for i in range(1,4):
        cadeau_list.append(input(f'cadeau {i}: '))
        cadeautjes[naam] = cadeau_list
    if len(namen) >= 3:
        toevoegen = input('nog een naam toevoegen? ')

shuffle(namen)

for i in range(0,len(namen)):
    if i == len(namen)-1:
        lootjes[namen[i]] = namen[0]
    else:
        lootjes[namen[i]] = namen[i+1]

while True:
    opvragen = input('\nvan wie wil je het lootje weten? ')
    cadeau = ', '.join(cadeautjes[opvragen])
    print(f'{opvragen} is gekoppeld aan {lootjes[opvragen]} verzochten cadeautjes: {cadeau}')
    print()