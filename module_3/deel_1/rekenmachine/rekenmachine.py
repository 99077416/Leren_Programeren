import functions

choice = input('A getallen optellen \nB getallen aftrekken \nC getallen vermenigvuldigen \nD getallen delen \nE getal ophogen \nF getal verlagen \nG getal verdubbelen \nH getal halveren \nwat wilt u doen? ').lower()

efgh = ['e','f','g','h']


n1 = int(input('getal1: '))


while choice != 'i':
    if choice not in efgh:
        n2 = int(input('getal2: '))

    if choice == 'a':
        uitkomst = functions.addition(n1,n2)
        print(f'{n1} + {n2} = {uitkomst}')

    elif choice == 'b':
        uitkomst = functions.subtraction(n1,n2)
        print(f'{n1} - {n2} = {uitkomst}')

    elif choice == 'c':
        uitkomst = functions.multiplication(n1,n2)
        print(f'{n1} * {n2} = {uitkomst}')

    elif choice == 'd':
        uitkomst = functions.division(n1,n2)
        print(f'{n1} : {n2} = {uitkomst}')

    elif choice == 'e':
        uitkomst = functions.addition(n1,1)
        print(f'{n1} + {1} = {uitkomst}')

    elif choice == 'f':
        uitkomst = functions.subtraction(n1,1)
        print(f'{n1} - {1} = {uitkomst}')

    elif choice == 'g':
        uitkomst = functions.multiplication(n1,2)
        print(f'{n1} * {2} = {uitkomst}')

    elif choice == 'h':
        uitkomst = functions.division(n1,2)
        print(f'{n1} / {2} = {uitkomst}')

    n1 = uitkomst
    choice = ''
    while choice == '':
        choice = input(f'Wil je wat met de uitkomst ({uitkomst}) doen? \nA) iets optellen, \nB) iets aftrekken, \nC) met iets vermenigvuldigen, \nD) ergens door delen, \nE) ophogen, \nF) verlagen, \nG) verdubbelen, \nH) halveren of \nI) niets?').lower()
