lijst = []

def town(getal):
    string = ''
    for i in range(getal):
        string += f'Hello from function town {i+1}!\n'

    return string

print(town(3))