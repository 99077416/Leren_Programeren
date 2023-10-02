vrachtwagen_bewijs = input('heeft u een vrachtwagen rijbewijs? ja/nee ')
hoge_hoed = input('heeft u een hoge hoed? ja/nee ')
gewicht = int(input('hoe zwaar bent u in kg? '))
lengte = int(input('hoe lang bent u in cm? '))
Certificaat = input('heeft u Certificaat “Overleven met gevaarlijk personeel”? ja/nee ')
ervaring_dieren = int(input('hoeveel jaar heeft u ervaring met dieren? '))
ervaring_jongleren = int(input('hoeveel jaar heeft u ervaring met jongleren? '))
ervaring_acrobatiek = int(input('hoeveel jaar ervaring heeft u met acrobatiek? '))

MIN_GEWICHT = 90
MAX_GEWICHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
MIN_ERVARING_DIEREN = 4
MIN_ERVARING_JONGLEREN = 5
MIN_ERVARING_ACROBATIEK = 3

if vrachtwagen_bewijs == 'ja' and hoge_hoed == 'ja' and gewicht > MIN_GEWICHT and gewicht < MAX_GEWICHT and lengte > MIN_LENGTE and lengte < MAX_LENGTE and Certificaat == 'ja' and (ervaring_dieren > MIN_ERVARING_DIEREN or ervaring_jongleren > MIN_ERVARING_JONGLEREN or ervaring_jongleren > MIN_ERVARING_JONGLEREN or ervaring_acrobatiek > MIN_ERVARING_ACROBATIEK):
    print('u mag solliciteren.')
else:
    print('u mag helaas niet solliciteren.')
