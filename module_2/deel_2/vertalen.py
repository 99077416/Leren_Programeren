
dict = {}

dict['hart'] = 'ingang'
dict['schubben'] = 'teennagels'
dict['vurige'] = 'waterende'
dict['draak'] = 'geit'
dict['vlammenzee'] = 'golf van water'
dict['schild'] = 'zwemvliezen'
dict['magie'] = 'plastic'

#text = input('text: ')
text = 'In het hart van de grot zagen ze Draganthor, met zijn glinsterende schubben en vurige ogen. De draak brulde en spuwde een vlammenzee die hen bedreigde, maar Rurik beschermde hen met een krachtig schild van magie'

split = text.split()

teller = -1

for i in split:
    teller +=1
    if i in dict:
        split[teller] = dict[i]

join = ' '.join(split)

print()
print(join)
