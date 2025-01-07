PIZZA_OPTIONS = ('small','medium','large')
pizza_price = (10,15,20)
PRICE_SMALL = 10
PRICE_MEDIUM = 15
PRICE_LARGE = 20

YES_OPTIONS = ('j','J')
NO_OPTIONS = ('n','N')
YES_NO_OPTIONS = YES_OPTIONS + NO_OPTIONS

bestelling = {
    'small': 0,
    'medium': 0,
    'large': 0
}

def input_option(prompt, options):
  while True:
    answer = input(prompt+'\n')
    if answer in options:
      return answer
    else:
      print(f'Verwacht alleen optie uit: {" of ".join(options)}') 

def input_yes_no(prompt: str) -> str:
  return input_option(prompt,YES_NO_OPTIONS)

def input_size(prompt):
  return input_option(prompt,PIZZA_OPTIONS)

def input_int(prompt):
  while True:
    try:
        answer = input(prompt + '\n')
        amount = int(answer)
        return amount
    except ValueError:
      print(f'Geen geldig getal: {answer}')

def pizza_add(amount,size):
    bestelling[size] += amount

def print_totaal(bestelling):
    i = 0
    for key,value in enumerate(bestelling):
        print(key)
        print(value)
        if bestelling[value]>0:
            print(f'totaal {value}:      {bestelling[value]} * {pizza_price[i]} = {bestelling[value] * pizza_price[i]}')
        i +=1
    # totaal_small = bestelling['small'] * PRICE_SMALL
    # totaal_medium = bestelling['medium'] * PRICE_MEDIUM
    # totaal_large = bestelling['large'] * PRICE_LARGE
    # totaal = totaal_small + totaal_medium + totaal_large
    
    # print('\nKassabon')
    # print('='*30)

    # if bestelling['small']>0:
    #     print(f'totaal small:      {bestelling["small"]} * {PRICE_SMALL} = {totaal_small}')
    # if bestelling['medium']>0:
    #     print(f'totaal medium:     {bestelling["medium"]} * {PRICE_MEDIUM} = {totaal_medium}')
    # if bestelling['large']>0:
    #     print(f'totaal large:      {bestelling["large"]} * {PRICE_LARGE} = {totaal_large}')
    # print('='*30)
    # print(f'totaal                      {totaal}')
