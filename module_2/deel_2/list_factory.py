lijst = []

aantal = int(input('aantal lijsten: '))

len = []
for i in range(aantal):
    lengte = int(input(f'lengte lijst {i+1}: '))
    len.append(lengte)

X=1
for i in len:
    lijst.append(list(range(X,X*i+1,X)))
    X+=1
print(lijst)
