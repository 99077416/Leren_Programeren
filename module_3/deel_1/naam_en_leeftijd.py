def naam_en_leeftijd():

    naam = input('naam: ')
    leeftijd = input('leeftijd: ')
    woonplaats = input('woonplaats: ')
    
    dict = {
        'name' : naam,
        'age' : leeftijd,
        'city' : woonplaats
    }
    return dict

def vragen():
    door = ''
    list = []
    while door != 'stop':

        dict = naam_en_leeftijd()

        
        list.append(f"{dict['name']}, die in {dict['city']} woont, is {dict['age']} jaar")
        door = input('Toets enter om door te gaan of stop om te printen: ')
    return list



for i in vragen():
    print(i)