
for uur in range(24):
    printuur = uur
    if printuur > 12:
        printuur -= 12
    ampm = 'pm'

    if uur < 12:
        ampm = 'am'
        
    print(f'{printuur}{ampm}')