def main():    
    COLOR_NAMES = {
        'AliceBlue': '#f0f8ff',
        'AntiqueWhite': '#faebd7',
        'AntiqueWhite1': '#ffefdb',
        'AntiqueWhite3': '#cdc0b0',
        'AntiqueWhite4': '#8b8378',
        'aquamarine1': '#7fffd4',
        'aquamarine2': '#76eec6',
        'aquamarine4': '#458b74',
        'azure1': '	#f0ffff',
        'azure2': '#e0eeee'
    }
    #find longest key
    longestKey = max([len(key) for key in COLOR_NAMES.keys()])
    # print list
    for key, value in COLOR_NAMES.items():
        print('{:{}}: {}'.format(key,longestKey,value))
    # convert keys to lower
    LOWER_COLOR_NAMES = {key.lower(): value for key, value in COLOR_NAMES.items()}
    
    colorName = input('Enter name of color: ').lower()
    while colorName:
        if colorName in LOWER_COLOR_NAMES:
            print('{} - {}'.format(COLOR_NAMES[colorName].keys(),COLOR_NAMES[colorName]))  
        else: 
            print('Invalid')
        colorName = input('Enter name of color: ').lower()


main()