
pizza = input('wat voor pizza wilt u? small/medium/large ')

while True:
    try:
        aantal_pizza = int(input("hoeveel pizza's wilt u ")) 
        break
    except ValueError:
        print('ongeldig getal')

if pizza == 'small':
    prijs_pizza = 10
elif pizza == 'medium':
    prijs_pizza = 15
elif pizza == 'large':
    prijs_pizza = 20

totaal = prijs_pizza * aantal_pizza

print()
print(f"aantal pizza's: {aantal_pizza}, {pizza}")
print(f'totaalprijs: {totaal}')