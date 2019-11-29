import random


def main():
    numberOfScore = int(input("Enter number of scores: "))

    in_file = open('result.txt','a')

    for i in range(1, numberOfScore+1):
        score = random.randint(0, 100)
        in_file.write('{0}.score {1} is {2}\n'.format(i,score,determineScore(score)))
        print('{0} is {1}'.format(score,determineScore(score)))
    in_file.close


def determineScore(score):
    if score < 0:
        return "Invalid score"
    else:#jsdhkjsdh
        if score > 100:
            return "Invalid score"
        elif 90 > score >= 50:
            return "Passable"
        elif score >= 90:
            return "Excellent"
    if score < 50:
        return "Bad"

main()