def main():
    DICT = {}
    text = input('text: ')
    words = text.split()
    words.sort()
    # find longest key
    longestKey = max([len(word) for word in words])
    # count words and add to new DICT
    for word in words:
        if word in DICT:
            DICT[word] += 1
        else:
            DICT[word] = 1
    # print DICT
    for key, value in DICT.items():
        print('{:{}}: {}'.format(key,longestKey,value))

main()