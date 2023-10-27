from time import sleep
opnieuw = 'ja'

print('welkom bij mijn game')
sleep(2)
print()

while opnieuw == 'ja':
    while True:
        print('je wordt wakker door geschreeuw.')
        sleep(2)
        print('wat doe je?')
        sleep(0.5)
        geschreeuw = input('(1)kijk wat er aan de hand is.(2)ga terug naar bed. ')
        if geschreeuw == '2':
            print()
            print('je gaat terug naar bed.')
            sleep(2)
            print('je merkt niks, maar wordt vermoord in je slaap.')
            sleep(1)
            print('GAME OVER')
            break
        elif geschreeuw == '1':
            print()
            print('je kijkt uit je raam om te zien wat er gebeurt.')
            sleep(2)
            print()
            print('je ziet dat je dorp wordt aangevallen door trollen!')











    sleep(1)
    print()
    opnieuw = input('opnieuw proberen? ja/nee ')
