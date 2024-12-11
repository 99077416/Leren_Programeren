import random
import string
wachtwoord = []


all_lower = string.ascii_lowercase
all_upper = string.ascii_uppercase
all_numbers = '0123456789'
all_special = '@#$%_?'

all = all_lower + all_upper + all_numbers + all_special

lower = []
upper = []
numbers = []
special = []




for i in range(3):
    l = random.choice(all_lower+all_upper)
    wachtwoord.append(l)

for i in range(20):
    l = random.choice(all)
    wachtwoord.append(l)

l = random.choice(all_upper+all_numbers)
wachtwoord.append(l)




print(''.join(wachtwoord))


