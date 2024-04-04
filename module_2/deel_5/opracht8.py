from fruitmand2 import fruitmand
weight = 0
for i in fruitmand:
    weight +=i ['weight']

print(weight)
weight = 0

watermeloen = {
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
}

fruitmand.append(watermeloen)

for i in fruitmand:
    weight +=i ['weight']
    
print(weight)