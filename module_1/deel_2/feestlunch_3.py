PRIJS_CROISSANT = 0.39
aantal_croissant = int(input('hoeveel croissants? ')) 

PRIJS_STOKBROOD = 2.78
aantal_stokbrood = int(input('hoeveel stokbroden? '))

PRIJS_KORTINGSBON = 0.50
aantal_kortingsbon = int(input('hoeveel kortingsbonnen? '))



totaal_croissant = aantal_croissant * PRIJS_CROISSANT 
totaal_stokbrood = PRIJS_STOKBROOD * aantal_stokbrood
totaal_kortingsbon = PRIJS_KORTINGSBON * aantal_kortingsbon
totaal = totaal_croissant + totaal_stokbrood - totaal_kortingsbon

print(f'De feestlunch kost je bij de bakker {totaal} euro voor de {aantal_croissant} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbon} kortingsbonnen nog geldig zijn!')
