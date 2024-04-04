from fruitmand2 import fruitmand
lengte1 = 0
lengte = 0

for i in fruitmand:
    lengte1 = len(i['name'])
    if lengte1 > lengte:
        lengte = len(i['name'])
        fruit = i
        kleur = i['color']
        naam = i['name']
        gewicht = i['weight']


kleuren = {
    'red' : 'rood',
    'yellow' : 'geel',
    'orange' : 'oranje',
    'green' : 'groen',
    'brown' : 'bruin',
    'pink' : 'roze'
}

print(f'de "{naam}" ({lengte} letters) heeft een {kleuren[kleur]} kleur en een gewicht van {gewicht/1000} kg')