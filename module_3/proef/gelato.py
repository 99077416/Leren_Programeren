from functions import *
from data import * 

bestellen = 'ja'

print('Welkom bij PapiGelato je mag alle smaken kiezen zo lang het maar vanille ijs is.')

while bestellen == 'ja':
    while True:
        smaak = keuze_smaak('welke smaak wilt u? ')

        aantal = aantalBolletjes('Hoeveel bolletjes wilt u? ')

        if aantal > 8:
            print('Sorry, zulke grote bakken hebben we niet')

        elif aantal >= 4 and aantal <= 8:
            print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
            verpaking = 'bakje'
            break

        elif aantal >= 1 and aantal <=3:
            verpaking = keuze_verpaking(f'Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ')
            break
    
    print(f'Hier is uw {verpaking} met {aantal} bolletje(s).')
    bestelling['smaak'] = smaak
    bestelling['aantal'] = aantal
    bestellen = meer_bestellen('Wilt u nog meer bestellen? ')

print()
bon()
print('Bedankt en tot ziens!')
print()
print(bestelling)