from data import *

error_text = 'Sorry,dat snap ik niet...'

def aantalBolletjes(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_text)

def keuze_smaak(aantal):
    for i in range(1,aantal+1):
        while True:
            smaak = input(f'Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?')
            if smaak in smaken:
                toevoegen(smaken[smaak],1)
                break
            else:
                print(error_text)

def keuze_topping(aantal,verpaking):
    while True:
        topping = input(f'Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?')
        if topping in toppings:
            if topping == 'b':
                toevoegen(toppings[topping],prijs_slagroom)
            if topping == 'c':
                for i in range(aantal):
                    toevoegen(toppings[topping],prijs_sprinkels)
            if topping == 'd':
                if verpaking == 'hoorntje':
                    toevoegen(toppings[topping],prijs_caramel_hoorntje)
                if verpaking == 'bakje':
                    toevoegen(toppings[topping],prijs_caramel_bakje)
            break
        else:
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

    totaal = 0
    for i in smaken:
        if smaken[i] in bestelling:
            smaak = smaken[i]
            aantal_bolletjes = bestelling[smaak]
            totaal_bolletjes = round(aantal_bolletjes * prijs_bolletje,2)
            totaal += totaal_bolletjes
            print(f"{smaak}     {bestelling[smaak]} x €{prijs_bolletje} = € {totaal_bolletjes}")

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
    
    totaal_topping = 0
    for i in toppings:
        if toppings[i] in bestelling:
            topping = toppings[i]
            prijs_topping = bestelling[topping]
            totaal_topping += prijs_topping

    if totaal_topping > 0:
        print(f"Topping                 = € {totaal_topping}")
    totaal += totaal_topping

    print('                        --------- +')
    print(f'Totaal                  = € {round(totaal,2)}')