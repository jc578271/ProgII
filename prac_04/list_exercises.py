numbers = [5, 20, 1, 2, 3]

print('The first number is: ', numbers[0])
print('The last number is: ', numbers[-1])
print('The smallest number is: ', min(numbers))
print('The largest number is: ', max(numbers))
print('The average number is: ', sum(numbers) / len(numbers))

# username
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input('Enter username: ')
if username in usernames:
    print('Access granted')
else:
    print('Access denied')