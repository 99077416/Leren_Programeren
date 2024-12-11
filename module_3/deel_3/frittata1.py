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
print(f'{round_piece(amount_eggs)} {TXT_EGGS}')
print(f'{round_quarter(amount_milk)} {UNIT_CUPS} {TXT_MILK}')
print(f'{round_quarter(amount_salt)} {UNIT_TEASPOONS} {TXT_SALT}')
print(f'{round_quarter(amount_pepper)} {UNIT_TEASPOONS} {TXT_PEPPER}')
print(f'{round_quarter(amount_oil)} {UNIT_SPOONS} {TXT_OIL}')
print(f'{round_piece(amount_onions)} {TXT_ONIONS}')
print(f'{round_piece(amount_garlics)} {TXT_GARLICS}')
print(f'{round_quarter(amount_spinach)} {TXT_SPINACH}')
print(f'{round_piece(amount_paprikas)} {UNIT_CUPS} {TXT_PAPRIKAS}')
print(f'{round_quarter(amount_cheese)} {UNIT_CUPS} {TXT_CHEESE}')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print('-----------------------------------------------')