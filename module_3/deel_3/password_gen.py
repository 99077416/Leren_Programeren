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


x = random.randint(2,6)
for i in range(x):
    l = random.choice(all_upper)
    upper.append(l)

for i in range(8):
    l = random.choice(all_lower)
    lower.append(l)

for i in range(3):
    l = random.choice(all_special)
    special.append(l)

x = random.randint(4,7)
for i in range(x):
    l = random.choice(all_numbers)
    numbers.append(l)

wachtwoord += lower + upper + numbers + special

random.shuffle(wachtwoord)

leng = len(wachtwoord)
mid = leng//2

if leng != 24:
    diff = 24 - leng
    for i in range(diff):
        wachtwoord.insert((mid), random.choice(all_lower))

go = False

while go == False:
    if wachtwoord[0] in all_special:
        l = wachtwoord.pop(0)
        wachtwoord.insert(mid,l)

    elif wachtwoord[-1] in all_special or wachtwoord[-1] in all_lower:
        l = wachtwoord.pop(-1)
        wachtwoord.insert(mid,l)

    elif wachtwoord[mid] in all_upper:
        l = wachtwoord.pop(mid)
        wachtwoord.insert(0,l)

    elif wachtwoord[mid+1] in all_upper:
        l = wachtwoord.pop(mid+1)
        wachtwoord.insert(0,l)

    else:
        go = True

print(''.join(wachtwoord))
print(len(wachtwoord))