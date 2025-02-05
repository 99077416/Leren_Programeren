error_text = 'Sorry dat is geen optie die we aanbieden... '

def aantalBolletjes(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_text)

def keuze_smaak(aantal,smaken,klant,bestelling):
    if klant == 1:
        type = 'bolletje'
    elif klant == 2:
        type = 'liter'
    for i in range(1,aantal+1):
        while True:
            smaak = input(f'Welke smaak wilt u voor {type} nummer {i}? A) Aardbei, C) Chocolade of V) Vanille? ')

            if smaak in smaken:
                toevoegen(smaken[smaak],1,bestelling)
                break
            else:
                print(error_text)

def keuze_topping(aantal,verpaking,toppings,prijzen,bestelling):
    while True:
        topping = input(f'Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ')
        if topping in toppings:
            if topping == 'b':
                toevoegen(toppings[topping],prijzen['slagroom'],bestelling)
            if topping == 'c':
                for i in range(aantal):
                    toevoegen(toppings[topping],prijzen['sprinkels'],bestelling)
            if topping == 'd':
                if verpaking == 'hoorntje':
                    toevoegen(toppings[topping],prijzen['caramel hoorntje'],bestelling)
                if verpaking == 'bakje':
                    toevoegen(toppings[topping],prijzen['caramel bakje'],bestelling)
            break
        else:
            print(error_text)

def toevoegen(product,aantal,bestelling):
    if product in bestelling:
        bestelling[product] += aantal
    else:
        bestelling[product] = aantal
    return bestelling

def keuze_verpaking(prompt,verpaking_keuze):
    while True:
        keuze = input(prompt)
        if keuze in verpaking_keuze:
            return keuze
        else:
            print(error_text)

def meer_bestellen(prompt,bestellen_keuze):
    while True:
        keuze = input(prompt)
        if keuze in bestellen_keuze:
            return keuze
        else:
            print(error_text)

def bon(bestelling,smaken,toppings,prijzen,klant):
    print('---------["Papi Gelato"]---------\n')
    if klant == 1:
        totaal = 0
        for i in smaken:
            if smaken[i] in bestelling:
                smaak = smaken[i]
                aantal_bolletjes = bestelling[smaak]
                totaal_bolletjes = round(aantal_bolletjes * prijzen['bolletje'],2)
                totaal += totaal_bolletjes
                print(f"B.{smaak:10} {aantal_bolletjes:3.0f} x €{prijzen['bolletje']:0.2f} = €{totaal_bolletjes:0.2f}")

        if 'hoorntje' in bestelling:
            aantal_hoorntjes = bestelling['hoorntje']
            totaal_hoorntjes = round(aantal_hoorntjes * prijzen['hoorntje'],2)
            totaal += totaal_hoorntjes
            print(f"{'Hoorntjes':10} {aantal_hoorntjes:5.0f} x €{prijzen['hoorntje']:0.2f} = €{totaal_hoorntjes:0.2f}")

        if 'bakje' in bestelling:
            aantal_bakjes = bestelling['bakje']
            totaal_bakjes = aantal_bakjes * prijzen['bakje']
            totaal += totaal_bakjes
            print(f"{'Bakjes':10} {aantal_bakjes:5.0f} x €{prijzen['bakje']:0.2f} = €{totaal_bakjes:0.2f}")
        
        totaal_topping = 0
        for i in toppings:
            if toppings[i] in bestelling:
                topping = toppings[i]
                prijs_topping = bestelling[topping]
                totaal_topping += prijs_topping

        if totaal_topping > 0:
            print(f"{'Topping':25}= €{totaal_topping:0.2f}")
        totaal += totaal_topping
        print(f"{'':20}   ---------")
        print(f"{'Totaal':25}= €{round(totaal,2)}")
    elif klant == 2:
        totaal = 0
        for i in smaken:
            if smaken[i] in bestelling:
                smaak = smaken[i]
                aantal_liter = bestelling[smaak]
                prijs_liter = prijzen['liter']
                totaal_liter = round(aantal_liter * prijs_liter,2)
                totaal += totaal_liter
                print(f"L.{smaak:10}  {aantal_liter:3.0f} x €{prijs_liter:0.2f} = €{totaal_liter:3.2f}")
        btw = totaal_liter / 100 * 6

        print(f"{'':25}---------")
        print(f"{'Totaal':25} = €{totaal:0.2f}")
        print(f"{'btw':25} = €{btw:0.2f}")
