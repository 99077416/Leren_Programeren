from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('how many people? ') # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS

# calculate amount_eggs
amount_eggs = AMOUNT_EGGS * factor
# calculate amount_milk
amount_milk = AMOUNT_MILK * factor
# calculate amount_salt
amount_salt = AMOUNT_SALT * factor
# calculate amount_pepper
amount_pepper = AMOUNT_PEPPER * factor
# calculate amount_oil
amount_oil = AMOUNT_OIL * factor
# calculate amount_onions
amount_onions = AMOUNT_ONIONS * factor
# calculate amount_garlics
amount_garlics = AMOUNT_GARLICS * factor
# calculate amount_spinach
amount_spinach = AMOUNT_SPINACH * factor
# calculate amount_paprikas
amount_paprikas = AMOUNT_PAPRIKAS * factor
# calculate amount_cheese
amount_cheese = AMOUNT_CHEESE * factor
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')



print(f'{round_piece(amount_eggs)} {str_single_plural(round_piece(amount_eggs),TXT_EGGS)}')
print(f'{str_amount_fraction(amount_milk)} {str_single_plural(amount_milk,TXT_CUPS)} {TXT_MILK} ({unit2ml(amount_milk,UNIT_MILK)} ml)')
print(f'{str_amount_fraction(amount_salt)} {str_single_plural(amount_salt, TXT_TEASPOONS)} {TXT_SALT} ({ml2gram(unit2ml(amount_salt,UNIT_SALT),GRAM_PER_ML_SALT)} gram)')
print(f'{str_amount_fraction(amount_pepper)} {str_single_plural(amount_pepper,TXT_TEASPOONS)} {TXT_PEPPER} ({ml2gram(unit2ml(amount_pepper,UNIT_PEPPER),GRAM_PER_ML_PEPPER)} gram)')
print(f'{str_amount_fraction(amount_oil)} {str_single_plural(amount_oil,TXT_SPOONS)} {TXT_OIL} ({unit2ml(amount_oil,UNIT_OIL)} ml)')
print(f'{round_piece(amount_onions)} {str_single_plural(round_piece(amount_onions),TXT_ONIONS)}')
print(f'{round_piece(amount_garlics)} {str_single_plural(round_piece(amount_garlics),TXT_GARLICS)}')
print(f'{round_piece(amount_paprikas)} {str_single_plural(round_piece(amount_paprikas),TXT_PAPRIKAS)}')
print(f'{str_amount_fraction(amount_spinach)} {str_single_plural(amount_spinach,TXT_CUPS)} {TXT_SPINACH} ({ml2gram(unit2ml(amount_spinach,UNIT_SPINACH),GRAM_PER_ML_SPINACH)} gram)')
print(f'{str_amount_fraction(amount_cheese)} {str_single_plural(amount_cheese,TXT_CUPS)} {TXT_CHEESE} ({ml2gram(unit2ml(amount_cheese,UNIT_CHEESE),GRAM_PER_ML_CHEESE)} gram)')

# print (formatted) all amounts and units combined with their ingrediënt descriptions
print('-----------------------------------------------')