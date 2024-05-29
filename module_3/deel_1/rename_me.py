def is_even(getal:int) -> bool:
    return getal % 2 == 0

def woorden_omdraaien(string:str) -> str:
    split = string.split()
    omdraaien = split[::-1]
    join = ' '.join(omdraaien)
    return join

def aantal_unieke_characters(string:str) -> int:
    veschillende_letters = set(string)
    aantal = len(veschillende_letters)
    return aantal

def gemiddelde_lengte_woorden(string:str) -> float:
    split = string.split()
    
    len_woorden = 0
    for woord in split:
        len_woorden += len(woord)

    gemiddelde = len_woorden / len(split)
    return gemiddelde

def tafel(getal:int, tafel:int=10) -> None:
    for som in range(1, tafel+1):
        uitkomst = som * getal
        print(f'{som} x {getal} = {uitkomst}')



print(is_even(1424))

print(woorden_omdraaien('woorden omdraaien'))

print(aantal_unieke_characters('woord123 4!@$!'))

print(gemiddelde_lengte_woorden('gemiddelde lengte van de woorden'))

tafel(9,5)

tafel(9)