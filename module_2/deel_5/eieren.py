eieren = ['roze','geel','groen','rood','blauw']

plekken = [9,0,4,6,3,9,10,7,-1,-70]


geen_ei = []

length = len(eieren)

for i in plekken:
    if i < length and i > -length:
        print(f'je hebt een {eieren[i]} ei gevonden')
    else:
        geen_ei.append(i)

print(geen_ei)
 