from fruitmand2 import fruitmand

kleuren = []

for i in range(0,len(fruitmand)):
    fruit = fruitmand[i]
    if fruit['color'] not in kleuren:
        kleuren.append(fruit['color'])

loop = True

while loop == True:

    kleur = input('kleur: ')

    if kleur in kleuren:
        loop = False
    else:
        print(f'De kleur {kleur} zit er niet in de fruitmand')

aantal_rond = 0
aantal_niet_rond = 0

for i in fruitmand:

    if i['round'] == True and i['color'] == kleur:
        aantal_rond += 1
    elif i['round'] == False and i['color'] == kleur:
        aantal_niet_rond += 1

if aantal_rond > aantal_niet_rond:
    verschil = aantal_rond - aantal_niet_rond
    print(f'Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif aantal_niet_rond > aantal_rond:
    verschil = aantal_niet_rond - aantal_rond
    print(f'Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif aantal_rond == aantal_niet_rond:
    print(f'Er zijn {aantal_rond} ronde vruchten en {aantal_niet_rond} niet ronde vruchten in de kleur {kleur}')
