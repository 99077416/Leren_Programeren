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

vrachtwagen_bewijs_ok = vrachtwagen_bewijs == 'ja'
hoge_hoed_ok = hoge_hoed == 'ja'
gewicht_ok = gewicht > MIN_GEWICHT and gewicht < MAX_GEWICHT
lengte_ok = lengte > MIN_LENGTE and lengte < MAX_LENGTE
Certificaat_ok = Certificaat == 'ja' 
ervaring_ok = ervaring_dieren > 4