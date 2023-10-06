print('denk aan een kaas.')
print()

antwoord_vraag_1 = input('is de kaas geel? ').lower()

if antwoord_vraag_1 == 'ja':
    antwoord_vraag_2 = input('zitten er gaten in? ').lower()
    if antwoord_vraag_2 == 'ja': 
        antwoord_vraag_3  = input('is de kaas belachelijk duur? ').lower()
        if antwoord_vraag_3 == 'ja':
            kaas = 'Emmenthaler'
        elif antwoord_vraag_3 == 'nee':
            kaas = 'leerdammer'
    else:
        antwoord_vraag_3 = input('is de kaas hard als steen?').lower()
        if antwoord_vraag_3 == 'ja':
            kaas = 'Parmigiano Reggiano'
        else:
            kaas = 'Goudse kaas'
else:
    if antwoord_vraag_1 == 'nee':
        antwoord_vraag_2 = input('heeft de kaas blauwe schimmel? ').lower()
        if antwoord_vraag_2 == 'ja':
            antwoord_vraag_3 = input('heeft de kaas korst? ').lower()
            if antwoord_vraag_3 == 'ja':
                kaas = 'Blue de Rochbaron'
            else:
                kaas = "Foume d'ambert"
        else:
            antwoord_vraag_3 = input('heeft de kaas korst? ').lower()
            if antwoord_vraag_3 == 'ja':
                kaas = 'Camenbert'
            else:
                kaas = 'Mozzarella'
print()
print(f'je denkt aan {kaas}')
