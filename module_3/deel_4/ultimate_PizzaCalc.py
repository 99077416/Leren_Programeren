from pizza_help import *

answer = input_yes_no('wilt u bestellen? (J/N)')

if answer in NO_OPTIONS:
    exit('Tot ziens!')

while answer in YES_OPTIONS:
    size = input_size('wat voor pizza wilt u? (small/medium/large)')

    aantal_pizza = input_int(f'hoeveel {size} pizzas wilt u bestellen?')

    pizza_add(aantal_pizza,size)

    answer = input_yes_no('wilt u nog een pizza bestellen? (J/N)')

print_totaal(bestelling)
