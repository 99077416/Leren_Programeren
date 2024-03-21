uur = 1

tijd = ''
while uur <= 24:
    if uur < 12 or uur == 24:
        tijd = 'am'
    else:
        tijd = 'pm'
    if uur <= 12:
        print(f'{uur} {tijd}')
    else:
        print(f'{uur-12} {tijd}')
    uur += 1