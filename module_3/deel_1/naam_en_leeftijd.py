def naam_en_leeftijd():

    naam = input('naam: ')
    leeftijd = input('leeftijd: ')
    woonplaats = input('woonplaats: ')
    
    persoon = {
        'name' : naam,
        'age' : leeftijd,
        'city' : woonplaats
    }
    return persoon


def vragen():
    door = ''
    personen = []
    while door != 'stop':
        personen.append(naam_en_leeftijd())
        door = input('Toets enter om door te gaan of stop om te printen: ')

    return personen