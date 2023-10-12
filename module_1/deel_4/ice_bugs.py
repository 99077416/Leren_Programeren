def convertToEuroText (amount):
    return "€{:.2f}".format(amount).replace(".", ",")

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

amount = int(input('Hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(SMALL_PRICE))))
amount_small = amount * SMALL_PRICE
amount = int(input('En hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(MEDIUM_PRICE))))
amount_medium = amount * MEDIUM_PRICE
totalPrice = amount_small + amount_medium
print('Dat is dan {} totaal'.format(convertToEuroText(totalPrice)))