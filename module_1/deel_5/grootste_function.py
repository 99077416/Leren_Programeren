
def meten(nr1,nr2):
    if nr1 == nr2:
        print('Beide getallen zijn even groot')
    elif nr1 > nr2:
        resultaat = f'Maximum: {nr1} en minimum: {nr2}'
    else:
        resultaat = f'Maximum: {nr2} en minimum: {nr1}'
    return resultaat


getal_1 = input('getal 1')
getal_2 = input('getal 2')

print(meten(getal_1,getal_2))

