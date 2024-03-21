lijst = ['50']
x = 51
som = 50
i = 1
while som < 1000:
    lijst.append(str(x))
    join = " + ".join(lijst)
    som += (x)
    print(f'{i}. {join} = {som}')
    i+=1
    x += 1
