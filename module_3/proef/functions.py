from data import *

error_text = 'Sorry,dat snap ik niet...'

def aantalBolletjes(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_text)

def toevoegen(product,aantal):
    if product in bestelling:
        bestelling[product] += aantal
    else:
        bestelling[product] = aantal

def keuze_verpaking(prompt):
    while True:
        keuze = input(prompt)
        if keuze in verpaking_keuze:
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
    print('---------["Papi Gelato"]---------\n')

    aantal_bolletjes = bestelling['bolletjes']
    totaal_bolletjes = round(aantal_bolletjes * prijs_bolletje,2)
    totaal = totaal_bolletjes
    print(f"Bolletjes     {aantal_bolletjes} x €{prijs_bolletje}  = € {totaal_bolletjes}")

    if 'hoorntje' in bestelling:
        aantal_hoorntjes = bestelling['hoorntje']
        totaal_hoorntjes = round(aantal_hoorntjes * prijs_hoorntje,2)
        totaal += totaal_hoorntjes
        print(f"Hoorntjes     {aantal_hoorntjes} x €{prijs_hoorntje} = € {totaal_hoorntjes}")

    if 'bakje' in bestelling:
        aantal_bakjes = bestelling['bakje']
        totaal_bakjes = round(aantal_bakjes * prijs_bakje,2)
        totaal += totaal_bakjes
        print(f"Bakjes        {aantal_bakjes} x €{prijs_bakje} = € {totaal_bakjes}")

    


    print('                        --------- +')
    print(f'Totaal                    € {totaal}')