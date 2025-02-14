from functions import *
from data import * 

bestellen = 'ja'

print('Welkom bij PapiGelato.')


while bestellen == 'ja':
    klant = int(input('Bent u 1) een particuliere klant of 2) een zakelijke klant? '))

    if klant == 1:
        
        while bestellen == 'ja':
            aantal = aantalBolletjes('Hoeveel bolletjes wilt u? ')

            if aantal > 8:
                print('Sorry, zulke grote bakken hebben we niet')

            else:
                keuze_smaak(aantal,smaken,klant,bestelling)

                if aantal >= 4 and aantal <= 8:
                    print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
                    verpaking = 'bakje'

                elif aantal >= 1 and aantal <=3:
                    verpaking = keuze_verpaking(f'Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ',verpaking_keuze)

                keuze_topping(aantal,verpaking,toppings,prijzen,bestelling)
                bestelling = toevoegen(verpaking,1,bestelling)

                print(f'Hier is uw {verpaking} met {aantal} bolletje(s).')

                bestellen = meer_bestellen('Wilt u nog meer bestellen? ',bestellen_keuze)

    elif klant == 2:

            aantal = aantalBolletjes('hoeveel liter ijs wilt u? ')
            keuze_smaak(aantal,smaken,klant,bestelling)
            break

    else:
        print(error_text)

bon(bestelling,smaken,toppings,prijzen,klant)
print()
print('Bedankt en tot ziens!')