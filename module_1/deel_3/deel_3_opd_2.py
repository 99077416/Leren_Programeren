print('denk aan een kaas.')
print()

vraag_1 = input('is de kaas geel? ').lower()

if vraag_1 == 'ja':
    vraag_2 = input('zitten er gaten in? ').lower()
    if vraag_2 == 'ja': 
        vraag_3  = input('is de kaas belachelijk duur? ').lower()
        if vraag_3 == 'ja':
            kaas = 'Emmenthaler'
        elif vraag_3 == 'nee':
            kaas = 'leerdammer'
    else:
        vraag_3 = input('is de kaas hard als steen?').lower()
        if vraag_3 == 'ja':
            kaas = 'Parmigiano Reggiano'
        else:
            kaas = 'Goudse kaas'
else:
    if vraag_1 == 'nee':
        vraag_2 = input('heeft de kaas blauwe schimmel? ').lower()
        if vraag_2 == 'ja':
            vraag_3 = input('heeft de kaas korst? ').lower()
            if vraag_3 == 'ja':
                kaas = 'Blue de Rochbaron'
            else:
                kaas = "Foume d'ambert"
        else:
            vraag_3 = input('heeft de kaas korst? ').lower()
            if vraag_3 == 'ja':
                kaas = 'Camenbert'
            else:
                kaas = 'Mozzarella'
print()
print(f'je denkt aan {kaas}')