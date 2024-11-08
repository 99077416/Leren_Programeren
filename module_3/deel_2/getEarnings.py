from functions import *

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(people)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(investors)
    goldCut = getAdventurerCut(profitGold,investorsCuts,people)

    # verdeel de uitkomsten
    for person in people:
        #code aanvullen
        earnings.append({
            'name'   : person['name'],
            'start'  : 0.0,
            'end'    : 0.0
        })

    return earnings
