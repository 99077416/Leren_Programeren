ochtend = 1
middag = 1

for a in range(0,12):
    print(f'{ochtend}am')
    ochtend += 1
    if ochtend > 12:
        for a in range(0,12):
            print(f'{middag}pm')
            middag += 1
