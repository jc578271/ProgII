"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
>> it will occur and print invalid number

2. When will a ZeroDivisionError occur?
>> it will occur and print 'cannot divide by zero'

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
>> Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
        pass
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
