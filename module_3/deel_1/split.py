from collections import Counter
import math, random

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}
    
def aantal_getallen(getallen):
    # aantal gettalen in de lijst
    aantal = len(getallen)
    return aantal

def som_getallen(getallen):
    # Som van alle getallen in de lijst
    som = sum(getallen)
    return som

def gemiddelde(som,aantal):
    # Gemiddelde berekenen
    gemiddelde = som / aantal
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
    
def delen1():
    # Het kleinste getal gedeeld door het eerste controle getal
    delen1 = kleinste_getal() / controlegetal1
    return delen1

def delen2():
    # Het grootste getal gedeeld door het tweede controle getal
    delen2 = grootste_getal() / controlegetal2
    return delen2

def unieke_getallen(getallen):
    # alle unieke getallen
    unieke_getallen = list(set(getallen))
    return unieke_getallen

def aantal_unieke_elementen():
    # Aantal unieke elementen in de lijst
    aantal_unieke_elementen = len(unieke_getallen())
    return aantal_unieke_elementen

def verschil1():
    # Verschil tussen aantal unieke elementen en eerste controle getal
    verschil = abs(aantal_unieke_elementen - controlegetal1)
    return verschil

def sorteer(getallen):
    # Sorteer de lijst van getallen
    gesorteerde_lijst = sorted(getallen)
    return gesorteerde_lijst

def sorteer_uniek():
    # Sorteer de lijst van unieke getallen
    gesorteerde_lijst_uniek = sorted(unieke_getallen())
    return gesorteerde_lijst_uniek

def aantal_uniek_in_lijst(getallen ):    
    # Tel het aantal keren dat elk uniek element voorkomt in de lijst
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer

def getallen_deelbaar1():
    # Getallen die deelbaar zijn door het eerste controlle getal
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)

def getallen_deelbaar2():
    # Getallen die deelbaar zijn door het tweede controlle getal
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)

def komtvoor_in_lijst(getallen):
    # Controleer of een bepaald getallen in de lijst voorkomen
    komtvoor = controlegetal1 in getallen and controlegetal2 in getallen

def pos_controlegetal1(getallen):
    # Vindt de posities van heteerste controle getal
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)

def standaardafwijking(getallen,aantal):
    # Standaardafwijking berekenen
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

def shuffle_lijst(getallen):
    # Shuffle de lijst
    random.shuffle(getallen)

def random_getal(getallen,aantal):
    # Pak een random getal uit de lijst
    random_getal = getallen[random.randint(0,aantal-1)]
    return random_getal

def veschil_getallen():
    # Verschil tussen twee getallen
    verschil2 = abs(random_getal - controlegetal2)

    resultaten = {
        "Aantal getallen": aantal_getallen(),
        "Gemiddelde": gemiddelde,
        "Som": som_getallen(),
        "Grootste getal": grootste_getal(),
        "Kleinste getal": kleinste_getal(),
        "Eerste getal": eerste_getal,
        f"{kleinste_getal} / {controlegetal1}": delen1,
        f"{grootste_getal} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen(),
        f"Het verschil tussen {aantal_unieke_elementen()} & {controlegetal1}": verschil1(),
        "Gesorteerde lijst getallen": sorteer(),
        "Gesorteerde lijst unieke getallen": sorteer_uniek(),
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": getallen,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")