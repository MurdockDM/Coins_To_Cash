def calc_dollars(**coins):
    dollarAmount = 0
    coinTotal = coins.items()
    for coinType, amount in coinTotal:
        if coinType == "pennies":
            dollarAmount += (amount*.01)
        elif coinType == "nickels":
            dollarAmount += (amount*.05)
        elif coinType == "dimes":
            dollarAmount += (amount*.10)
        elif coinType == "quarters":
            dollarAmount += (amount*.25)
    print(dollarAmount)
calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)
