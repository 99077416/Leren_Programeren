PERSONEN = int(input('hoeveel personen? '))
TICKET = int(input('prijs ticket in centen:'))

PRIJS_VR = int(input('prijs vr voor 5 minuten in centen:'))
TIJD_VR = int(input('hoeveel minuten vr? '))

totaal_ticket = TICKET * PERSONEN
totaal_vr = TIJD_VR * PRIJS_VR // 5

totaal = totaal_ticket + totaal_vr

print(f'Dit geweldige dagje-uit met {PERSONEN} mensen in de Speelhal met {TIJD_VR} minuten VR kost je maar {totaal} cent')
