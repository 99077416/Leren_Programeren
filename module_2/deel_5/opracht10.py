from fruitmand2 import fruitmand

fruitmand2 = sorted(fruitmand, key=lambda d: d['weight'], reverse=True)

for i in fruitmand2:
    print(f"{i['name']} {i['weight']}")