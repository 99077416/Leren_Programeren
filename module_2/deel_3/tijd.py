count = 0

while count < 24:
    printuur = count
    if printuur > 12:
        printuur -= 12
    ampm = 'pm'

    if count < 12:
        ampm = 'am'
    count +=1
    print(f'{printuur}{ampm}')