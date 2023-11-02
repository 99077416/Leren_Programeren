from time import sleep
from random import randint
opnieuw = 'ja'

print('welkom bij mijn game')
sleep(3)
print()

while opnieuw == 'ja':
    while True:
        print('je wordt wakker door geschreeuw.')
        sleep(2)
        print('wat doe je?')
        sleep(0.5)
        wakker = input('(1)kijk wat er aan de hand is.(2)ga terug naar bed. ')

        if wakker == '2':
            print()
            print('je gaat terug naar bed.')
            sleep(2)
            print('je merkt niks, maar wordt vermoord in je slaap.')
            sleep(1)
            print('GAME OVER')
            break

        elif wakker == '1':
            print()
            print('je kijkt uit je raam om te zien wat er gebeurt.')
            sleep(2)
            print()
            print('je ziet dat je dorp wordt aangevallen!')
            sleep(2)
            print('wat ga je doen?')
            aanval = input('(1)zoek een wapen. (2)probeer zo snel mogelijk uit het dorp te komen. ')
            
            if aanval == '1':
                print()
                print('je gaat naar buiten en zoekt naar een wapen.')
                sleep(1)
                steen = input('pak steen? ja/nee ')
                mes = input('pak mes? ja/nee ')
                touw = input('pak stukje touw? ja/nee ')
                print()
                print('waar ga je heen?')
                plan = input('(1)zoek de leider. (2)loop naar de uitgang. ')
                if plan == '1':
                    print()
                    print()                                                                #plan_2 = input('probeer ongezien te blijven? ja/nee ')
                    print('je kruipt tussen de struiken.')                                 #if plan_2 == 'ja':
                    sleep(2)
                    print()
                    print('er ligt een lange tak op de grond.')
                    sleep(1)
                    tak = input('neem tak mee? ja/nee ')
                    sleep(1)
                    if tak == 'ja':
                        if mes and touw == 'ja':
                            print()
                            print('je maakt een speer met je mes, tak en touw.')
                            speer = True
                            sleep(3)
                        else:
                            speer = False
                            print()
                            print('je zou een speer kunnen maken met een mes en een stukje touw.')
                            sleep(3)
                    elif tak == 'nee':
                        speer = False
                    print()
                    print('je ziet de leider staan.')
                    sleep(1)
                    print('er staat een bevijliger naast hem.')
                    print()
                    sleep(3)
                    if steen == 'ja':                         
                        print('je gooit de steen om de bevijliger af te leiden')           #afleiden = input('gooi steen om bevijliger af te leiden? ja/nee ')
                        steen = 'nee'
                        sleep(2)
                        print('de bevijliger loopt weg om te zien wat het was.')
                        sleep(2)
                        print()
                        print('wat doe je?')
                        if speer == True:
                            gokken = input('probeer speer naar de leider te gooien? ja/nee ')
                            if gokken == 'ja':
                                kans = randint(1,4)
                                gooi = randint(1,4)
                                print(kans)
                                print(gooi)
                                if kans == gooi:
                                    print()
                                    print('je gooit raakt!')
                                    sleep(2)
                                    print()
                                    print('je hebt de leider verslagen!')
                                    sleep(2)
                                    print('het leger trekt terug.')
                                    sleep(2)
                                    print('je hebt het dorp gered!')
                                    sleep(1)
                                    print('GEWONNEN!')
                                    break
                                else:
                                    print()
                                    sleep(1)
                                    print('je gooit voledig mis.')
                                    sleep(2)
                                    print('de bevijliger ziet je en maakt je dood.')
                                    sleep(2)
                                    print('GAME OVER')
                                    break
                        
                    vecht = input('(1)probeer dicht bij te komen. (2)geef op en ga het dorp uit. ')

                    if vecht == '1':
                        print()
                        print('je probeert dichter bij de leider te komen')
                        sleep(2)





            print()
            print('je gaat richting de uitgang van het dorp. ')
            sleep(1)






    sleep(1)
    print()
    opnieuw = input('opnieuw proberen? ja/nee ')
