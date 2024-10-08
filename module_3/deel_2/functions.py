import time
from termcolor import colored
from data import *
import math


##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    gold = personCash['gold']
    gold += copper2gold(personCash['copper'])
    gold += silver2gold(personCash['silver'])
    gold += platinum2gold(personCash['platinum'])
    return gold
##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    gold_per_day = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * people) 
    gold_per_day += copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY * horses) 

    foodcost = gold_per_day * JOURNEY_IN_DAYS
    return round(foodcost,2)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    key_list = []
    for person in list:
        if key in person:
            if person[key] == value:
                key_list.append(person)
    return key_list

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    
    share = getShareWithFriends(friends)
    return getAdventuringPeople(share)
    


##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people/2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people/3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    total_cost = silver2gold(COST_HORSE_SILVER_PER_DAY)* horses * JOURNEY_IN_DAYS
    total_cost += (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS/ 7)) * tents
    return total_cost

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    list = []
    for item in items:
        list.append(f'{item["amount"]}{item["unit"]} {item["name"]}')
    if len(list) > 1:
        text = " & ".join([", ".join(list[:-1]),list[-1]])
    else:
        text = list[0]
    return text

def getItemsValueInGold(items:list) -> float:
    value = 0
    for item in items:
        price = item['price']
        type = price['type']
        if type == 'copper':
            value += copper2gold(price['amount']) * item['amount']
        elif type == 'silver':
            value += silver2gold(price['amount']) * item['amount']
        elif type == 'platinum':
            value += platinum2gold(price['amount']) * item['amount']
        elif type == 'gold':
            value += price['amount'] * item['amount']
    return round(float(value),2)


##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    gold = 0
    for person in people:
        cash = person['cash']
        gold += getPersonCashInGold(cash)
    return float(round(gold,2))
        

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    list = []
    for investor in investors:
        profit = investor['profitReturn']
        if profit <= 10:
            list.append(investor)
    return list

def getAdventuringInvestors(investors:list) -> list:
    investors = getInterestingInvestors(investors)
    return getFromListByKeyIs(investors, 'adventuring', True)

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    adventuring_investors = getAdventuringInvestors(investors)
    people = len(adventuring_investors)
    total_cost = round(getItemsValueInGold(gear) * people,2)

    horses = people
    tents = people

    total_cost += silver2gold(COST_HORSE_SILVER_PER_DAY)* horses * JOURNEY_IN_DAYS
    total_cost += (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS/ 7)) * tents

    cost_per_day = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * people) 
    cost_per_day += copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY * horses) 

    total_cost += cost_per_day * JOURNEY_IN_DAYS

    return total_cost


##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()