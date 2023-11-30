aantal = int(input('aantal lijsten: '))
lengte = int(input('lengte lijsten: '))

for i in range(1,aantal):
    print(list(range(i,lengte+1,i)))