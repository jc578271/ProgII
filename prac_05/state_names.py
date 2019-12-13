"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = { "QLD": "Queensland", 
                "NSW": "New South Wales", 
                "NT": "Northern Territory",
                "WA": "Western Australia", 
                "ACT": "Australian Capital Territory", 
                "VIC": "Victoria", 
                "TAS": "Tasmania"
            }
# print(STATE_NAMES)
for key, value in STATE_NAMES.items():
    print('{:3}: {}'.format(key,value))

state = input("Enter short state: ").upper()

while state:   
    print('{} is {}'.format(state, STATE_NAMES[state])) if state in STATE_NAMES else print("Invalid short state")
    state = input("Enter short state: ")