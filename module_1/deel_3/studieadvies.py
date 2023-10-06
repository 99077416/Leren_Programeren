
print('''
*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds 
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies. 
''')

aantal_weken_vraag = int(input('Hoeveel weken ben je al bezig met de opleiding? '))
competentie_stelling_1 = int(input('''
Ik voel stress of blokkades bij het maken van programmeeropdrachten. 
Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit '''))

competentie_stelling_2 = int(input('''
Ik stel programmeeropdrachten en -uitdagingen uit.
Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit '''))

competentie_stelling_3 = int(input('''
Ik denk dat ik geen talent heb voor de opleiding. 
Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit '''))

competentie_stelling_4 = int(input('''
Ik vermijd assessments (CJV) en feedback van kritische docenten. 
Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit '''))

competentie_stelling_5 = int(input('''
Ik vergelijk mezelf met anderen die beter lijken te zijn.
Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit '''))

if aantal_weken_vraag >= 10:
    competentie_stelling_6 = int(input('''
    Ik voel geen interesse in nieuwe programmeertechnieken.
    Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit '''))

    competentie_stelling_7 = int(input('''
    Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.
    Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit '''))

score = competentie_stelling_1 + competentie_stelling_2 + competentie_stelling_3 + competentie_stelling_4 + competentie_stelling_5
gemidelde_score = score // 5
if aantal_weken_vraag >= 10:
    score = score + competentie_stelling_6 + competentie_stelling_7
if aantal_weken_vraag >= 10:
    gemidelde_score = score // 7

COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''

stellingen = []
stellingen.append(competentie_stelling_1)
stellingen.append(competentie_stelling_2)
stellingen.append(competentie_stelling_3)
stellingen.append(competentie_stelling_4)
stellingen.append(competentie_stelling_5)
if aantal_weken_vraag > 10:
    stellingen.append(competentie_stelling_6)
    stellingen.append(competentie_stelling_7)



altijd = 0
vaak = 0
regelmatig = 0


if competentie_stelling_1 == '0':
    altijd = altijd + 1
elif competentie_stelling_1 == '1':
    vaak = vaak + 1
elif competentie_stelling_1 == '2':
    regelmatig = regelmatig + 1

if competentie_stelling_2 == '0':
    altijd = altijd + 1
elif competentie_stelling_2 == '1':
    vaak = vaak + 1
elif competentie_stelling_2 == '2':
    regelmatig = regelmatig + 1

if competentie_stelling_3 == '0':
    altijd = altijd + 1
elif competentie_stelling_3 == '1':
    vaak = vaak + 1
elif competentie_stelling_3 == '2':
    regelmatig = regelmatig + 1

if competentie_stelling_4 == '0':
    altijd = altijd + 1
elif competentie_stelling_4 == '1':
    vaak = vaak + 1
elif competentie_stelling_4 == '2':
    regelmatig = regelmatig + 1

if competentie_stelling_5 == '0':
    altijd = altijd + 1
elif competentie_stelling_5 == '1':
    vaak = vaak + 1
elif competentie_stelling_5 == '2':
    regelmatig = regelmatig + 1

if aantal_weken_vraag > 10:
    if competentie_stelling_6 == '0':
        altijd = altijd + 1
    elif competentie_stelling_6 == '1':
        vaak = vaak + 1
    elif competentie_stelling_6 == '2':
        regelmatig = regelmatig + 1

    if competentie_stelling_7 == '0':
        altijd = altijd + 1
    elif competentie_stelling_7 == '1':
        vaak = vaak + 1
    elif competentie_stelling_7 == '2':
        regelmatig = regelmatig + 1



COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''



print('''
*********************** STUDIEADVIES ***********************
''')
if gemidelde_score <= 2 or (altijd or vaak) > len(stellingen) / 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)

elif gemidelde_score <= 3 or (altijd or vaak or regelmatig) > len(stellingen) / 2:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)

else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
