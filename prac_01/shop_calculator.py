while True:
    amountItems = int(input("Number of items: "))
    if amountItems < 0:
        print('Invalid number of items!')
    else:
        totalPrice = 0
        for i in range(1, amountItems + 1):
            while True:
                priceItem = float(input("Price of item: "))
                if priceItem < 0:
                    print('Invalid value!')
                else:
                    totalPrice += priceItem
                    break
        if totalPrice > 100:
            totalPrice = totalPrice * 0.9
        print('Total price of {} items is $'.format(amountItems), totalPrice)
        break
