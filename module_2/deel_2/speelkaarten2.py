from random import shuffle
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']

kaarten = ['aas','boer','vrouw','heer']

deck = ['joker', 'joker']

for i in range(2,11):
    for kleur in kleuren:
        deck.append(f'{kleur} {i}')

for i in kleuren:
    for kaart in kaarten:
        deck.append(f'{i} {kaart}')

shuffle(deck)

for i in range(1,8):
    card = deck.pop(0)
    print(f'kaart {i}: {card}')

print()
print(f'deck ({len(deck)}): {deck}')