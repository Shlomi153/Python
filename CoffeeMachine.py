#TODO:
"""1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer."""

#TODO
'''2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.'''

#TODO
'''3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5'''

#TODO
'''4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
'''

#TODO
'''5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 10 cent, 20 cent, 50 cent, 1 Euro, 2 Euro'''

#TODO
'''6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5'''

#TODO
'''c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.'''

#TODO
'''7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
'''

import CoffeeMachineMenu
import os

def hasEnoughResources(ingredients, resources):
    for k, v in resources.items():
        for j, l in ingredients.items():
            if(k == j):
               if(v < l):
                   print(f'Sorry, there is not enough resources to make the drink.')
                   return False
    return True

def processCoins(price, currency):
    insert = 'y'
    sum = 0
    tenCent = 0.10
    twentyCent = 0.20
    fiftyCent = 0.50
    oneEuro = 1.00
    twoEuro = 2.00

    while(insert == 'Y'.lower()):
        addCoins = input(f'Please insert coins for your drink, total price: {price}{currency}.\nCoins we accept: 10, 20, 50 cents, 1 or 2 Euro:\nCancel to go back:\n')
        if(addCoins == '10'):
            sum += tenCent
        elif(addCoins == '20'):
            sum += twentyCent
        elif(addCoins == '50'):
            sum += fiftyCent
        elif(addCoins == '1'):
            sum += oneEuro
        elif(addCoins == '2'):
            sum += twoEuro
        elif(addCoins == 'cancel'):
            break
        else:
            print('Wrong input!')
            continue
        sum = round(sum, 2)
        print(f'Total inserted: {sum}.')

        insertAnother = 'y'
        while(insertAnother == 'Y'.lower()):
            insertAnother = input('Would you like to insert another coin?Y/N\n')
            if(insertAnother != 'N'.lower() or insertAnother != 'Y'.lower()):
               break
            else:
               print('Wrong input!')
        if(insertAnother == 'N'.lower()):
            break
    return sum

def transactionSuccessful(moneyInserted, price, profit):
    change = 0
    hasEnough = True
    if(moneyInserted >= price):
        print('Transaction successful!')
        profit += price
        change = round(moneyInserted - price,2)
    else:
        print(f'Sorry that''s not enough money. Money refunded.')
        hasEnough = False

    return profit, change, hasEnough

def returnChange(change, currency):
    print(f'Here is your change, a total of: {change}{currency}.')

def makeDrink(resourcesToMakeDrink, resources):
    res = {key: resources[key] - resourcesToMakeDrink.get(key, 0) for key in resources}
    print(f'Here is your {userChoice}. Enjoy!')

    return res


resources = menu.resources
resourcesCopy = resources.copy()
menu = menu.MENU

espresso = menu.get('espresso')
espressoIngredients = espresso.get('ingredients')
espressoCost = espresso.get('cost')

latte = menu.get('latte')
latteIngredients = latte.get('ingredients')
latteCost = latte.get('cost')

cappuccino = menu.get('cappuccino')
cappuccinoIngredients = cappuccino.get('ingredients')
cappuccinoCost = cappuccino.get('cost')

sufficientResources = False
currency = '€'
price = 0
profit = 0
userChoice = ''
resourcesToMakeDrink = {}

while(userChoice != 'off'.lower()):
    userChoice = input('What would you like? (espresso/latte/cappuccino)')
    if(userChoice == 'espresso'):
        sufficientResources = hasEnoughResources(espressoIngredients, resourcesCopy)
        price = espressoCost
        resourcesToMakeDrink = espressoIngredients.copy()
    elif(userChoice == 'latte'):
        sufficientResources = hasEnoughResources(latteIngredients, resourcesCopy)
        price = latteCost
        resourcesToMakeDrink = latteIngredients.copy()
    elif(userChoice == 'cappuccino'):
        sufficientResources = hasEnoughResources(cappuccinoIngredients, resourcesCopy)
        price = cappuccinoCost
        resourcesToMakeDrink = cappuccinoIngredients.copy()
    elif(userChoice == 'report'.lower()):
        print('Current resources:')
        for k, v in resourcesCopy.items():
            print(k, v)
        print(f'Profit: {profit}{currency}')

        input('Press any key to continue')
        os.system("cls")
        continue
    elif(userChoice == 'Off'.lower()):
        break

    else:
        print('Wrong input!')
        continue

    if(sufficientResources == False):
        print('Please pick another drink.')
        continue
    else:
        processCoinsSum = processCoins(price, currency)

    profit, change, hasEnough = transactionSuccessful(processCoinsSum, price, profit)

    if(hasEnough == False):
        continue

    if(change > 0):
        returnChange(change, currency)

    resourcesCopy = makeDrink(resourcesToMakeDrink, resourcesCopy)

    anotherDrink = input('Would you like to order another drink?y/n\n')
    if(anotherDrink == 'n'):
        break

print('Turning coffee machine off...')


