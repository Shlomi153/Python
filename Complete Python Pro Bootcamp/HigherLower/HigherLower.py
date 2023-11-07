import Logo
import GameData
import random
import os

#Format the account data into printable format
def formatOption(optionA, optionB):
    lA = []
    lB = []

    for k, v in optionA.items():
        optionDetailsA = f"{k.title()}: {v}"
        lA.append(optionDetailsA)

    for k, v in optionB.items():
        optionDetailsB = f"{k.title()}: {v}"
        lB.append(optionDetailsB)
    
    return lA, lB

#CompareFollowerCount
def compareFollowers(optionAFollowers,optionBFollowers):
    if(optionAFollowers > optionBFollowers):
        return 1
    elif(optionAFollowers < optionBFollowers):
        return 2
    elif(optionA == optionB):
        return 'equal'
    else:
        return 'error'

#Print in a clean format
def printOptions(lA, lB):
    
    print(Logo.logo)
    
    for i in lA:
        print(i)

    print(Logo.vs)

    for i in lB:
        print(i)

#Get user input
def userGuess(optionA, optionB):
    print('Which of the following do you think has more followers?\n')
    userGuess = input(f"1 for {optionA}\n2 for {optionB}\n")

    return userGuess

##########################################################################################################################

data = GameData.data
score = 0

#Inital picks, random data from GameDate module
optionA = random.choice(data)
optionB = random.choice(data)

locA = data.index(optionA)

del data[locA]

while(score != -1):
    #Compare options    
    comparison = compareFollowers(optionA['follower_count'], optionB['follower_count'])

    #Clean format
    cleanListA, cleanListB = formatOption(optionA, optionB)

    #Ask the user which has more followers
    userChoice = userGuess(optionA['name'], optionB['name'])

    #Check if user input is correct
    if(comparison == 'error'):
        print('Something went wrong!')
        break
    elif(comparison == 'equal'):
        score +=1
        print(f'They are both equal!\nTotal score so far: {score}\nBelow you can see the full comparison:')
        printOptions(cleanListA, cleanListB)
    elif(int(comparison) == int(userChoice)):
        score += 1
        print(f'Correct!\nTotal score so far: {score}\nBelow you can see the full comparison:')
        printOptions(cleanListA, cleanListB)
    else:
        print(f'Wrong, game over!\nTotal score: {score}\nBelow you can see the full comparison:')
        printOptions(cleanListA, cleanListB)
        score = -1
        break

    #Prepare comparison data for next round, put the winner in optionA
    locB = data.index(optionB)

    del data[locB]

    if(len(data) == 0):
        print(f'Congratulations, you have won the game!\nYour total score is: {score}.')
        break
    elif(comparison == 'equal'):
        optionB = random.choice(data)
    elif(int(comparison) == 2):
        optionA = optionB
    optionB = random.choice(data)

    #Put a waiting option for the user between rounds and clear the screen after each
    input('Press any key to continue.')
    os.system('cls')
     







