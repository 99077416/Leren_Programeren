from random import randint
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']

deck = ['joker', 'joker']

schud = []

for i in range(2,11):
    deck.append(f'harten {i}')
    deck.append(f'klaveren {i}')
    deck.append(f'schoppen {i}')
    deck.append(f'ruiten {i}')

for i in kleuren:
    deck.append(f'{i} aas')
    deck.append(f'{i} boer')
    deck.append(f'{i} vrouw ')
    deck.append(f'{i} heer')

for i in range(53,0,-1):
    kaart = randint(0,i)
    schud.append(deck[kaart])
    deck.remove(deck[kaart])
    
schud.append(deck[0])

for i in range(7):
    print(f'kaart {i+1}: {schud[i]}')

for i in range(7):
    schud.remove(schud[0])
print()
print(f'deck ({len(schud)}): {schud}')