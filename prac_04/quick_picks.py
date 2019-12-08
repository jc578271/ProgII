import random

MIN = 1
MAX = 45

quickPick = int(input('how many quick pick: '))

for line in range (quickPick):
    numbersInALine = []
    for i in range(6):
        number = random.randint(MIN,MAX)
        while number in numbersInALine:
            number = random.randint(MIN,MAX)
        numbersInALine.append(number)
    numbersInALine.sort()
    for number  in numbersInALine:
        print('{:>2}'.format(number), end = ' ')
    print()

    
    

