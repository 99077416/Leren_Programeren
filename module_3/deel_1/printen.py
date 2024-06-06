from naam_en_leeftijd import vragen

personen_lijst = vragen()

for persoon in personen_lijst:
    print(f"{persoon['name']}, die in {persoon['city']} woont, is {persoon['age']} jaar. ")