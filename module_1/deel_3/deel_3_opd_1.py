getal_a = int(input('voer getal in: '))
getal_b = int(input('voer getal in: '))

if getal_a > getal_b: 
    max = getal_a
    min = getal_b
    print(f'a is het grootste getal: {max}')
elif getal_a < getal_b:
    max = getal_b
    min = getal_a
    print(f'a is het kleinste getal: {min}')
else:
    if getal_a == getal_b:
        print('a en b zijn even groot') 
        max = getal_a
        min = getal_b

print(f'Het minimum is: {min}')
print(f'Het maximum is: {max}')
