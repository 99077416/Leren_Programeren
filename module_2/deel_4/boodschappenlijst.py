
dict = {}
vraag = 'ja'

while vraag == 'ja':
    artikel = input('welk artikel wilt u toevoegen. ').lower()
    aantal = int(input(f'hoeveel {artikel} wilt u toevoegen? '))
    if artikel in dict:
        dict[f'{artikel}'] += aantal
    else:
        dict[f'{artikel}'] = aantal
    vraag = input('wilt u nog iets toevoegen? ')




print('-[ BOODSCHAPPENLIJST ]-')
print()
for i in dict:
    print(f'{dict[i]}x {i}')
print()
print('-----------------------')
