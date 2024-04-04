from random import randint
eindscore = 0
verschil = 0
ronde = 0

while ronde <= 20:
    ronde += 1
    teraden = randint(1,1000)
    poging = 0
    score = 0
    while poging < 10:
        poging += 1
        print()
        print(f'poging: {poging}')
        geraden = int(input('raad getal '))
        if teraden > geraden:
            verschil = teraden - geraden
        elif geraden > teraden:
            verschil = geraden - teraden

        if geraden == teraden:
            score += 1
            poging = 11
        else:
            if geraden < teraden:
                print('hoger')
            else:
                print('lager')
            if verschil < 50:
                if verschil < 20:
                    print('heel warm')
                else:
                    print('warm')
    eindscore += score
    print(f'score: {score}')
    opnieuw = input('nog een keer raden? ')
    if opnieuw == 'nee':
        break

print(eindscore)