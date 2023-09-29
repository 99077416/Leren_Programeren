PRIJS_CROISSANT = int(input('prijs croissant in centen: '))
AANTAL_CROISSANT = int(input('hoeveel croissants? ')) 

PRIJS_STOKBROOD = int(input('prijs stokbrood in centen: '))
AANTAL_STOKBROOD = int(input('hoeveel stokbroden? '))

PRIJS_KORTINGSBON = int(input('prijs kortingsbon in centen: '))
AANTAL_KORTINGSBON = int(input('hoeveel kortingsbonnen? '))



totaal_croissant = AANTAL_CROISSANT * PRIJS_CROISSANT 
totaal_stokbrood = PRIJS_STOKBROOD * AANTAL_STOKBROOD
totaal_kortingsbon = PRIJS_KORTINGSBON * AANTAL_KORTINGSBON
totaal = totaal_croissant + totaal_stokbrood - totaal_kortingsbon

print(f'De feestlunch kost je bij de bakker {totaal} cent voor de {AANTAL_CROISSANT} croissantjes en de {AANTAL_STOKBROOD} stokbroden als de {AANTAL_KORTINGSBON} kortingsbonnen nog geldig zijn!')
