PRIJS_CROISSANT = 0.39
AANTAL_CROISSANT = 17

PRIJS_STOKBROOD = 2.78 
AANTAL_STOKBROOD = 2

PRIJS_KORTINGSBON = 0.50
AANTAL_KORTINGSBON = 3

totaal_croissant = AANTAL_CROISSANT * PRIJS_CROISSANT 
totaal_stokbrood = PRIJS_STOKBROOD * AANTAL_STOKBROOD
totaal_kortingsbon = PRIJS_KORTINGSBON * AANTAL_KORTINGSBON
totaal = totaal_croissant + totaal_stokbrood - totaal_kortingsbon

print(f'De feestlunch kost je bij de bakker {totaal} euro voor de {AANTAL_CROISSANT} croissantjes en de {AANTAL_STOKBROOD} stokbroden als de {AANTAL_KORTINGSBON} kortingsbonnen nog geldig zijn!')