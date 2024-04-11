from fruitmand2 import fruitmand

# for fruit in fruitmand:
#     if fruit['name'] == 'druif':
#         fruitmand.remove(fruit)



# for i in range(0,len(fruitmand)):
#     if fruitmand[i]['color'] not in kleuren:
#         kleuren.append(fruitmand[i]['color'])
#         print(fruitmand[i]['color'])

kleuren = []

for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)
    elif fruit['color'] not in kleuren:
        kleuren.append(fruit['color'])
        print(fruit['color'])