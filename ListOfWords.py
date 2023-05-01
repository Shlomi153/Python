import random

def ListOfWords():

    animals = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat']

    cars = ['suzuki', 'mitsubishi', 'mazerati', 'mazda', 'seat', 'ferrari', 'porshe', 'fiat', 'renault', 'bmw']

    colors = ['blue', 'black', 'white', 'yellow', 'white', 'purple', 'grey', 'green', 'gold', 'silver', 'fuschia',
              'red', 'orange']

    countries = ['france', 'germany', 'belgium', 'portugal', 'spain', 'netherlands', 'luxembourg', 'austria',
                 'czech', 'poland', 'africa', 'usa', 'russia']

    listOfCategories = [animals, cars, colors, countries]

    randomCategory = random.choice(listOfCategories)
    randomValue = random.choice(randomCategory)
    randomLen = len(randomValue)

    output = randomValue, randomLen

    return output
