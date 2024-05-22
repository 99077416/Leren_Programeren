from collections import Counter
import math, random


    
def aantal_getallen(getallen):
    # aantal gettalen in de lijst
    aantal = len(getallen)
    return aantal

def som_getallen(getallen):
    # Som van alle getallen in de lijst
    som = sum(getallen)
    return som

def gemiddelde(getallen):
    # Gemiddelde berekenen
    gemiddelde = som_getallen(getallen) / aantal_getallen(getallen)
    return gemiddelde

def grootste_getal(getallen):
    # Het grootste getal in de lijst
    grootste_getal = max(getallen)
    return grootste_getal

def kleinste_getal(getallen):
    # Het kleinste getal in de lijst
    kleinste_getal = min(getallen)
    return kleinste_getal

    
def eerste_getal(getallen):
    # Het eerste getal in de lijst
    eerste_getal = getallen[0]
    return eerste_getal
    
def delen1(getallen,controlegetal1):
    # Het kleinste getal gedeeld door het eerste controle getal
    delen1 = kleinste_getal(getallen) / controlegetal1
    return delen1

def delen2(getallen,controlegetal2):
    # Het grootste getal gedeeld door het tweede controle getal
    delen2 = grootste_getal(getallen) / controlegetal2
    return delen2

def unieke_getallen(getallen):
    # alle unieke getallen
    unieke_getallen = list(set(getallen))
    return unieke_getallen

def aantal_unieke_elementen(getallen):
    # Aantal unieke elementen in de lijst
    aantal_unieke_elementen = len(unieke_getallen(getallen))
    return aantal_unieke_elementen

def verschil1(getallen,controlegetal1):
    # Verschil tussen aantal unieke elementen en eerste controle getal
    verschil = abs(aantal_unieke_elementen(getallen) - controlegetal1)
    return verschil

def sorteer(getallen):
    # Sorteer de lijst van getallen
    gesorteerde_lijst = sorted(getallen)
    return gesorteerde_lijst

def sorteer_uniek(getallen):
    # Sorteer de lijst van unieke getallen
    gesorteerde_lijst_uniek = sorted(unieke_getallen(getallen))
    return gesorteerde_lijst_uniek

def aantal_uniek_in_lijst(getallen ):    
    # Tel het aantal keren dat elk uniek element voorkomt in de lijst
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen
    

def deelbaar1(getallen,controlegetal1):
    # Getallen die deelbaar zijn door het eerste controlle getal
    deelbaar1 = []
    for getal in unieke_getallen(getallen):
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return deelbaar1

def deelbaar2(getallen,controlegetal2):
    # Getallen die deelbaar zijn door het tweede controlle getal
    deelbaar2 = []
    for getal in unieke_getallen(getallen):
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)
    return deelbaar2

def komtvoor_in_lijst(getallen,controlegetal1,controlegetal2):
    # Controleer of een bepaald getallen in de lijst voorkomen
    komtvoor = controlegetal1 in getallen and controlegetal2 in getallen
    return komtvoor

def posities(getallen,controlegetal1):
    # Vindt de posities van heteerste controle getal
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

def standaardafwijking(getallen):
    # Standaardafwijking berekenen
    verschil_kwadraat = sum((x - gemiddelde(getallen)) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal_getallen(getallen)
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

def shuffle_lijst(getallen):
    # Shuffle de lijst
    random.shuffle(getallen)
    return getallen

def random_getal(getallen):
    # Pak een random getal uit de lijst
    random_getal = getallen[random.randint(0,aantal_getallen(getallen)-1)]
    return random_getal

def verschil_getallen(getallen,controlegetal2):
    # Verschil tussen twee getallen
    verschil2 = abs(random_getal(getallen) - controlegetal2)
    return verschil2





def resultaat(getallen:list,controlegetal1:int,controlegetal2:int) -> dict:

    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}

    resultaten = {
        "Aantal getallen": aantal_getallen(getallen),
        "Gemiddelde": gemiddelde(getallen),
        "Som": som_getallen(getallen),
        "Grootste getal": grootste_getal(getallen),
        "Kleinste getal": kleinste_getal(getallen),
        "Eerste getal": eerste_getal(getallen),
        f"{kleinste_getal(getallen)} / {controlegetal1}": delen1(getallen,controlegetal1),
        f"{grootste_getal(getallen)} / {controlegetal2}": delen2(getallen,controlegetal2),
        "Aantal unieke elementen": aantal_unieke_elementen(getallen),
        f"Het verschil tussen {aantal_unieke_elementen(getallen)} & {controlegetal1}": verschil1(getallen,controlegetal1),
        "Gesorteerde lijst getallen": sorteer(getallen),
        "Gesorteerde lijst unieke getallen": sorteer_uniek(getallen),
        "Telling van elementen": aantal_uniek_in_lijst(getallen),
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1(getallen,controlegetal1),
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2(getallen,controlegetal2),
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor_in_lijst(getallen,controlegetal1,controlegetal2),
        f"{controlegetal1} komt voor op positie(s)": posities(getallen,controlegetal1),
        "Standaardafwijking": standaardafwijking(getallen),
        "Geshufflede lijst": shuffle_lijst(getallen),
        "Willekeurige getal uit de lijst": random_getal(getallen),
        f"Het verschil tussen {random_getal(getallen)} & {controlegetal2}": verschil_getallen(getallen,controlegetal2),
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:

getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal_1 = 8
controlegetal_2 = 3

analyse_resultaat = resultaat(getallenlijst, controlegetal_1, controlegetal_2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")