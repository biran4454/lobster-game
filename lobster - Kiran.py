from random import randint

weatherHist = []
day = 0
week = 0
balance = 100
billPayed = False
pots = 6
boats = 1
inshore = 0
offshore = 0
insurance = 0
def clearScreen():
    for i in range(35):
        print()
def weather():
    if len(weatherHist) > 2:
        if weatherHist[-3] == weatherHist[-2] and weatherHist[-2] == weatherHist[-1] and weatherHist[-1] == "b":
            weatherHist.append("h")
            return "h"
    w = randint(1, 6)
    if len(weatherHist) > 0 and weatherHist[-1] == "b" and w == 5 or w == 6:
        weatherHist.append("b")
    elif w == 6:
        weatherHist.append("b")
    else:
        weatherHist.append("g")
    return weatherHist[-1]

def dayCount(day, week):
    day += 1
    if day % 7 == 0:
        day = 0
        week += 1
    return day, week
def isNumber(a):
    try:
        b = int(a)
    except:
        return False
    return True
def askNumber(question):
    print(question)
    answer = ""
    while True:
        answer = input(">>> ")
        if isNumber(answer):
            return int(answer)
        print("Please enter a number")
def askBool(question):
    print(question)
    answer = ""
    while True:
        answer = input(">>> ")
        if len(answer) > 0 and answer[0].lower() == "y" or answer[0].lower() == "n":
            return answer[0].lower()
        print("Please enter y or n")

while True:
    clearScreen()
    day, week = dayCount(day, week)
    print("======== %i ========" % day)
    weather()
    print("Money:", balance)
    print("Weather:", weatherHist[-1])
    if insurance > 0:
        insurance -= 1
    if weatherHist[-1] == "h":
        print("There was a hurricane. You lost your boats and pots!")
        boats = 0
        if insurance > 1:
            insurance -= min(7, insurance)
            print("Your insurance company buys you a new boat")
            boats = 1
            balance += 20
            print("Your insurance company also gives you £20 for pots")
        else:
            if balance > 150:
                balance -= 150
                boats = 1
                print("You buy a boat and pots for £150")
            elif pots > 25:
                print("You cannot buy a new boat")
                print("You sell some pots to buy a new boat")
                pots -= 26
            else:
                print("You cannot buy a new boat")
                print("You don't have enough pots to sell")
            continue
    else:
        if inshore + offshore > 0:
            print("You collect your pots.")
            income = 0
            cost = 0
            if weatherHist[-1] == "b":
                income += 4 * inshore
                pots += inshore
            else:
                income += 2.5 * inshore
                income += 5 * offshore
                pots += inshore
                pots += offshore
            inshore = 0
            offshore = 0
            balance += income
            print("You earn £%i and are left with £" % income, balance, sep="")
    if day == 5 and billPayed == False:
        if balance > 80:
            balance -= 80
            print("You pay off your weekly maintenance costs")
        elif pots > 13:
            print("You cannot pay off your maintenance costs")
            print("You sell some pots to repair your boat")
            pots -= 13
            balance = 0
        else:
            print("You cannot pay off your maintenance costs")
            print("You have no pots to sell")
    if day == 5 or day == 6:
        continue
    if balance // 6 > 0 and askBool("Would you like to buy more pots?") == "y":
        print("You can buy up to %i pots, which cost £6 each" % (balance // 6))
        buyPots = min(askNumber("How many pots do you want to buy?"), balance // 6)
        pots += buyPots
        balance -= buyPots * 6
    if balance > 80 and billPayed == False and day > 2:
        if askBool("Would you like to pay your maintenance costs early?") == "y":
            balance -= 80
            billPayed = True
            print("You pay off your weekly maintenance costs")
    print("Here is the weather for today:", weatherHist[-1])
    if len(weatherHist) > 1:
        print("Here is the recent weather:")
        for i in range(min(len(weatherHist) - 1, 3)):
            print("==>", weatherHist[-2 - i])
    if balance >= 10 and askBool("Would you like to buy insurance?") == "y":
        insCost = 0
        if len(weatherHist) > 2 and weatherHist[-1] == "b" and weatherHist[-2] == "b" and weatherHist[-3] == "b":
            insCost = 100
        elif len(weatherHist) > 1 and weatherHist[-1] == "b" and weatherHist[-2] == "b":
            insCost = 50
        elif weatherHist[-1] == "b":
            insCost = 20
        elif len(weatherHist) > 1 and weatherHist[-2] == "b":
            insCost = 10
        else:
            insCost = 5
        print("7 days of insurance will cost £", insCost * 7, sep='')
        add = max(askNumber("How many days of insurance do you want to purchase?"), 0)
        if balance // (insCost * add) < 1:
            print("You don't have enough money for that.")
        else:
            insurance += add
            balance -= add * insCost
            print("You purchased %i days of insurance" % add)
            print("You now have %i days of insurance" % insurance)
            print("You now have £%i" % balance)
    print("You have %i pots" % pots)
    if pots == 0 or boats == 0 or askBool("Do you want to go fishing?") == "n":
        balance += 15
        print("You work in the hotel and earn £15")
        continue
    inshore = min(askNumber("How many inshore pots do you want to place?"), pots)
    pots -= inshore
    print("You place %i inshore pots" % inshore)
    print("Remaining pots:", int(pots))
    if pots > 0:
        offshore = min(askNumber("How many offshore pots do you want to place?"), pots)
        pots -= offshore
        print("You place %i offshore pots" % offshore)
        print("Remaining pots:", int(pots))
    



