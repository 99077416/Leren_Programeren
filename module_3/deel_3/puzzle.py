reeks = [1]
print(reeks)

for i in range(10):
    list = []
    num1 = reeks[0]
    count = 0
    for number in reeks:
        if number == num1:
            count += 1
        else:
            list.append(count)
            list.append(num1)
            num1 = number
            count = 1
    list.append(count)
    list.append(num1)
    reeks = list
    print(reeks)