from fruitmand import fruitmand

for i in range(len(fruitmand)-1,-1,-1):
    fruit = fruitmand[i]
    print(fruit['name'])

for fruit in fruitmand[::-1]: #sublist[van:tot:stapgroote] (van/tot leeg = begin/einde)
    print(fruit['name'])