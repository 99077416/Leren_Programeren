from functions import *
from data import * 

bestellen = 'ja'

print('Welkom bij PapiGelato.')



while bestellen == 'ja':
    while True:

        aantal = aantalBolletjes('Hoeveel bolletjes wilt u? ')

        keuze_smaak(aantal)

        if aantal > 8:
            print('Sorry, zulke grote bakken hebben we niet')

        elif aantal >= 4 and aantal <= 8:
            print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
            verpaking = 'bakje'
            break

        elif aantal >= 1 and aantal <=3:
            verpaking = keuze_verpaking(f'Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ')
            break
    
    
    toevoegen(verpaking,1)

    print(f'Hier is uw {verpaking} met {aantal} bolletje(s).')

    bestellen = meer_bestellen('Wilt u nog meer bestellen? ')

print()
bon()
print()
print('Bedankt en tot ziens!')