
def fibonacci(aantal):
    lijst = [0,1]
    for i in range(aantal):
        num1 = lijst[-1]
        num2 = lijst[-2]
        num3 = num1 + num2
        lijst.append(num3)

    gs = num1/num2
    return gs

aantal = int(input('aantal: '))

print(fibonacci(aantal))