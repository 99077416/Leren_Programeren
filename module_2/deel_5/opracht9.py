from fruitmand2 import fruitmand

for i in fruitmand:
    if i['name'] == 'druif':
        fruitmand.remove(i)

kleuren = []

for i in range(0,len(fruitmand)):
    if fruitmand[i]['color'] not in kleuren:
        kleuren.append(fruitmand[i]['color'])
        print(fruitmand[i]['color'])