gastheer = input('wie is de gastheer? ')
GASTEN = 5
drank = True
chips = True

if gastheer == 'mathis' or gastheer != 'slemmer' and drank == True or (gastheer != 'slemmer' or gastheer != 'slemmer' and GASTEN >= 4 and GASTEN <= 20) and chips == True and drank == True :
    print('Start the Party')
else:
    print('No Party')
