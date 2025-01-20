from data import *

error_text = 'Sorry,dat snap ik niet...'

def aantalBolletjes(prompt):
    while True:
        try:
            return int(input(prompt)) 
        except ValueError:
            print(error_text)

def keuze_verpaking(prompt):
    while True:
        keuze = input(prompt)
        if keuze in verpaking_keuze:
            return keuze
        else:
            print(error_text)

def keuze_smaak(prompt):
    while True:
        keuze = input(prompt)
        if keuze in smaken:
            return keuze
        else:
            print(error_text)

def meer_bestellen(prompt):
    while True:
        keuze = input(prompt)
        if keuze in bestellen_keuze:
            return keuze
        else:
            print(error_text)

def bon():

    prijs = prijzen[bestelling['smaak']]
    aantal = bestelling['aantal']
    totaal = prijs * aantal
    print(f'{aantal} bolletjes {bestelling["smaak"]} : {totaal}')
    print(f'totaal : {totaal}')
    