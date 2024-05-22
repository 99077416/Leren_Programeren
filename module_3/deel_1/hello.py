lijst = []

def town(getal):
    string = ''
    for i in range(1,getal+1):
        string += f'Hello from function town {i}!\n'

    return string

print(town(3))   