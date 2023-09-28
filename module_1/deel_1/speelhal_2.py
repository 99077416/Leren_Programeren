PERSONEN = 4
TICKET = 7.45

PRIJS_VR = 0.37 / 5
TIJD_VR = 45

TOTAAL_TICKET = TICKET * PERSONEN
TOTAAL_VR = TIJD_VR * PRIJS_VR

TOTAAL = TOTAAL_TICKET + TOTAAL_VR

print(f'Dit geweldige dagje-uit met {PERSONEN} mensen in de Speelhal met {TIJD_VR} minuten VR kost je maar {TOTAAL} euro')