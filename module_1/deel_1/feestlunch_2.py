prijs_croissant = 0.39
aantal_croissant = 17

prijs_stokbrood = 2.78 
aantal_stokbrood = 2

prijs_kortingsbon = 0.50
aantal_kortingsbon = 3

totaal_croissant = aantal_croissant * prijs_croissant 
totaal_stokbrood = prijs_stokbrood * aantal_stokbrood
totaal_kortingsbon = prijs_kortingsbon * aantal_kortingsbon
totaal = totaal_croissant + totaal_stokbrood - totaal_kortingsbon

print(f'De feestlunch kost je bij de bakker {totaal} euro voor de {aantal_croissant} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbon} kortingsbonnen nog geldig zijn!')