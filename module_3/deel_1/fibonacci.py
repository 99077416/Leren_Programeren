
def fibonacci(aantal:int):
    lijst = [0,1]
    for i in range(aantal):
        lijst.append(lijst[-1] + lijst[-2])

    return lijst

def gulden_snede(lijst:list):

    gs = lijst[-1] / lijst[-2]
    return gs


aantal = int(input('aantal: '))

print(fibonacci(aantal))

print(gulden_snede(fibonacci(aantal)))