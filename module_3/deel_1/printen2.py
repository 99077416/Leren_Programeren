from naam_en_leeftijd import vragen

personen_lijst = vragen()

for persoon in personen_lijst:
    print(f'In {persoon['city']} woont de {persoon['age']} jarige {persoon['name']}')