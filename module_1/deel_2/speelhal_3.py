personen = int(input('hoeveel personen? '))
PRIJS_TICKET = 7.45

PERIODE = 10
PRIJS_VR_PERIODE = 0.54
tijd_vr = int(input('hoeveel minuten vr? '))


totaal_ticket = PRIJS_TICKET * personen
totaal_vr = round(tijd_vr * PRIJS_VR_PERIODE / PERIODE,2)

totaal = totaal_ticket + totaal_vr

print(f'Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {tijd_vr} minuten VR kost je maar {totaal} euro')
