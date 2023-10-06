vrachtwagen_bewijs = input('heeft u een vrachtwagen rijbewijs? ja/nee ')
hoge_hoed = input('heeft u een hoge hoed? ja/nee ')
gewicht = int(input('hoe zwaar bent u in kg? '))
lengte = int(input('hoe lang bent u in cm? '))
Certificaat = input('heeft u Certificaat “Overleven met gevaarlijk personeel”? ja/nee ')
ervaring_dieren = int(input('hoeveel jaar heeft u ervaring met dieren? '))
ervaring_jongleren = int(input('hoeveel jaar heeft u ervaring met jongleren? '))
ervaring_acrobatiek = int(input('hoeveel jaar ervaring heeft u met acrobatiek? '))

diploma = input('bent u in bezit van een diploma MBO 4? ja/nee ')
ondernemer = input('bent u ondernemer? ja/nee ')
if ondernemer == 'ja':
    ervaring_ondernemer = int(input('hoeveel jaar bent u ondernemer? '))
    werknemers = int(input('hoeveel werknemers heeft u? '))
geslacht = input('wat is uw geslacht? man/vrouw/anders ')

if geslacht == 'vrouw':
    haar_kleur = input('welke kleur is uw haar? ')
    lengte_haar = int(input('hoelang is uw haar in cm? '))
    snor = False
    glimlach = False
elif geslacht == 'man':
    snor = int(input('hoe breed is uw snor in cm? '))
    haar_kleur = False
    lengte_haar = False
    glimlach = False
elif geslacht == 'anders':
    glimlach = int(input('hoe breed is uw glimlach in cm? '))
    snor = False 
    haar_kleur = False
    lengte_haar = False

print()

MIN_GEWICHT = 90
MAX_GEWICHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
MIN_ERVARING_DIEREN = 4
MIN_ERVARING_JONGLEREN = 5
MIN_ERVARING_ACROBATIEK = 3

MIN_ERVARING_ONDERNEMER = 3
MIN_WERKNEMERS = 5
MIN_LENGTE_SNOR = 10
MIN_LENGTE_HAAR = 20
MIN_LENGTE_GLIMLACH = 10



vrachtwagen_bewijs_ok = vrachtwagen_bewijs == 'ja'
hoge_hoed_ok = hoge_hoed == 'ja'
gewicht_ok = gewicht >= MIN_GEWICHT and gewicht < MAX_GEWICHT
lengte_ok = lengte >= MIN_LENGTE and lengte < MAX_LENGTE
Certificaat_ok = Certificaat == 'ja' 
ervaring_ok = ervaring_dieren >= MIN_ERVARING_DIEREN or ervaring_jongleren >= MIN_ERVARING_JONGLEREN or ervaring_acrobatiek >= MIN_ERVARING_ACROBATIEK

ondernemer_ok = ondernemer == 'ja'and ervaring_ondernemer > MIN_ERVARING_ONDERNEMER and werknemers > MIN_WERKNEMERS
diploma_ok = diploma == 'ja' or ondernemer_ok
snor_ok = snor > MIN_LENGTE_SNOR
haar_kleur_ok = haar_kleur == 'rood'
lengte_haar_ok = lengte_haar > MIN_LENGTE_HAAR
glimlach_ok = glimlach > MIN_LENGTE_GLIMLACH
geslacht_ok = snor_ok or (haar_kleur_ok and lengte_haar_ok) or glimlach_ok


if vrachtwagen_bewijs_ok and hoge_hoed_ok and gewicht_ok and lengte_ok and Certificaat_ok and ervaring_ok and diploma_ok and geslacht_ok:
    print('u mag solliciteren.')
else:
    print('u mag helaas niet solliciteren.')

print()

if vrachtwagen_bewijs_ok == False:
    print('u heeft een vrachtwagen rijbewijs nodig.')
if hoge_hoed_ok == False:
    print('u heeft een hoge hoed nodig.')
if gewicht_ok == False:
    print(f'uw gewicht moet minimaal {MIN_GEWICHT}kg zijn en maximaal {MAX_GEWICHT}kg.')
if lengte_ok == False:
    print(f'uw lengte moet minimaal {MIN_LENGTE}cm zijn en maximaal {MAX_LENGTE}cm.')
if Certificaat_ok == False:
    print('u heeft het certificaat "Overleven met gevaarlijk personeel" nodig.')
if ervaring_ok == False:
    print(f'u heeft minimaal {MIN_ERVARING_DIEREN} jaar ervaring met dieren of {MIN_ERVARING_JONGLEREN} jaar ervaring met jongleren of {MIN_ERVARING_ACROBATIEK} jaar ervaring met acrobatiek nodig.')
if diploma_ok == False:
    print(f'u heeft een diploma nodig van mbo-4 of ondernemer zijn met minimaal {MIN_WERKNEMERS} werknemers.')
if geslacht_ok == False:
    if geslacht == 'man':
        print(f'als man moet uw snor breder dan {MIN_LENGTE_SNOR}cm lang zijn')
    elif geslacht == 'vrouw':
        print(f'als vrouw moet uw haarkleur rood zijn en uw haar langer dan {MIN_LENGTE_HAAR}cm zijn.')
    elif geslacht == 'anders': 
        print(f'als ander geslacht moet uw glimlach breder {MIN_LENGTE_GLIMLACH}cm zijn.')
