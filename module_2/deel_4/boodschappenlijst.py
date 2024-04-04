
boodschappen = {}
toevoegen = 'ja'

while toevoegen == 'ja':
    artikel = input('welk artikel wilt u toevoegen. ').lower()
    aantal = int(input(f'hoeveel {artikel} wilt u toevoegen? '))
    if artikel in boodschappen:
        boodschappen[f'{artikel}'] += aantal
    else:
        boodschappen[f'{artikel}'] = aantal
    toevoegen = input('wilt u nog iets toevoegen? ')




print('-[ BOODSCHAPPENLIJST ]-')
print()
for i in boodschappen:
    print(f'{boodschappen[i]}x {i}')
print()
print('-----------------------')
