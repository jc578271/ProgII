# 1. 2.
in_file = open('name.txt', 'w')
name = str(input('name: '))
in_file.write(name)
in_file.close
in_file = open('name.txt', 'r')
name = in_file.read()
print('Your name is ',name)

# 3.
numberFile = open('number.txt', 'w')

numOne = 17
numTwo = 42
numberFile.write('{} \n'.format(numOne))
numberFile.write('{} \n'.format(numTwo))
numberFile.close

numberFile = open('number.txt', 'r')
num1 = numberFile.readline()
num2 = numberFile.readline()
total = int(num1) + int(num2)
print(total)
numberFile.close

#4. 

total1 = 0
randomFile = open('you.txt', 'r')
readFile = randomFile.readlines()
for line in readFile:
    try:
        total1 += int(line)
    except ValueError:
        continue
print(total1)

