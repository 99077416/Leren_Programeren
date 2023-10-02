gastheer = input('wie is de gastheer? ')
gasten = 5
drank = True
chips = True

if gastheer == 'mathis' or gastheer != 'slemmer' and drank == True or gastheer != 'slemmer' and gasten >= 4 and gasten <= 20 and chips == True and drank == True :
    print('Start the Party')
else:
    print('No Party')
