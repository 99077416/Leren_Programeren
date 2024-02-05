lijst = ['50']
x = 51
som = 50
while som < 1000:
    lijst.append(str(x))
    join = " + ".join(lijst)
    som += (x)
    print(f'{join} = {som}')
    x += 1

