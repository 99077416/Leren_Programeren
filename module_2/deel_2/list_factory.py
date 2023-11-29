aantal = int(input('aantal lijsten: '))
lengte = int(input('lengte lijsten: '))

for i in range(aantal):
    print(list(range(i+1,lengte,i+1)))