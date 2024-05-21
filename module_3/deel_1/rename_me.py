def is_even(getal:int) -> bool:
    return getal % 2 == 0

def string_omdraaien(string:str) -> str:
    split = string.split()
    omdraaien = split[::-1]
    join = ' '.join(omdraaien)
    return join

def aantal_verschillende_letters(string:str) -> int:
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

