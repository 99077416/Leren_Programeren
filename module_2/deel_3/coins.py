# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

dictionary = {}
toPay = int(float(input('Amount to pay: ')) * 100) # hoeveel het product kost
paid = int(float(input('Paid amount: ')) * 100) # hoeveel de klant heeft betaald
change = paid - toPay # berekend wat je terug moet geven

if change > 0: # als je nog wat moet terug geven
  coinValue = 500 # waarde van het geld
  
  while change > 0 and coinValue > 0: # als je nog wat moet terug geven
    nrCoins = change // coinValue # hoeveel je moet terug geven

    if nrCoins > 0: # als je nog wat moet terug geven
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print hoeveel je terug moet geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # invullen wat je hebt terug gegeven
      change -= nrCoinsReturned * coinValue # nieuw wisselgeld berekenen
      dictionary[coinValue] = nrCoinsReturned
# comment on code below: 
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #  als je het geld niet hebt terug gegeven
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done') 
  print()
  print('terug gegeven:')

#Print na de while loop ook een overzicht van alle teruggegeven muntstukken:
#per soort muntstuk hoeveel zijn er teruggeven.
  for muntsoort in dictionary:
    print(f'{dictionary[muntsoort]} munten van {muntsoort} ')

  # for i in range(len(list)):
  #   print(f'{list[i]}  {value[i]}')