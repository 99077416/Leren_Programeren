PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
stempel = False
#bouw hieronder de floowchart na

age = int(input('hoe oud ben je? '))
x = 21 - age
toegang_jaar = 18 - age
if age < 18:
    print('sorry je mag niet naar binnen.')
    print(f'probeer het in {toegang_jaar} jaar nog eens')

else:
    naam = input('wat is je naam? ')
    if naam in VIP_LIST:
        if age >= 21:
            bandje = 'blauw'
        else:
            bandje = 'rood'
        print(f'je krijgt van mij een {bandje} bandje')
    else:
        bandje = False
        if age >= 21:
            print('je krijgt van mij een stempel')
            stempel = True

            


    drank = input('wat wil je drinken? ')
    if drank in DRANKJES:
        if drank == 'champagne':
            if bandje:
                if bandje == 'blauw':
                    print(f'alstublieft je {drank}, dat is dan €{PRIJS_CHAMPAGNE}')
                else:
                    print('sorry je mag geen alcohol bestellen onder de 21')
                    print(f'probeer het in {x} jaar nog eens')
                    
            else:
                print('sorry aleen vips mogen champagne kopen.')


        elif drank == 'bier':
            if stempel or bandje:
                if bandje:
                    print('alstublieft, complimenten van het huis')
                else:
                    print(f'alstublieft je {drank}, dat is dan €{PRIJS_BIER} ')
            else:
                print('sorry je mag geen alcohol bestellen onder de 21')
                print(f'probeer het in {x} jaar nog eens')
        elif drank == 'cola':
            if bandje:
                    print('alstublieft, complimenten van het huis')
            else:
                print(f'alstublieft je {drank}, dat is dan €{PRIJS_BIER} ')
                
        
    else:
        print('sorry geen idee wat je bedoeld, hier een glaasje water.')
    