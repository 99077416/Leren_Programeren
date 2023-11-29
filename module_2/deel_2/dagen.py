week = ('maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag')

werkdagen = week[0], week[1], week[2], week[3], week[4]

weekend = week[5], week[6]

week_omgekeerd = tuple(reversed(week))

werkdagen_omgekeerd = tuple(reversed(werkdagen))

weekend_omgekeerd = tuple(reversed(weekend))

print()
print(f'Alle dagen van de week zijn: {week}')
print()
print(f'De werkdagen zijn: {werkdagen}')
print()
print(f'De weekenddagen zijn: {weekend}')
print()
print(f'Alle dagen van de week in omgekeerde volgorde zijn: {week_omgekeerd}')
print()
print(f'De werkdagen in omgekeerde volgorde zijn: {werkdagen_omgekeerd}')
print()
print(f'De weekenddagen in omgekeerde volgorde zijn: {weekend_omgekeerd}')
print()
