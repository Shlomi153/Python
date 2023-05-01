import random
from os import system

BlackjackLogo = '''
__________.__                 __         __               __    
\______   \  | _____    ____ |  | __    |__|____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /    |  \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \\  \___|    <     |  |/ __ \\  \___|    < 
 |______  /____(____  /\___  >__|_ \/\__|  (____  /\___  >__|_ \\
        \/          \/     \/     \/\______|    \/     \/     \/
'''

#Blackjack Game

#Difficulty Normal: Use all hints below
#Difficulty Hard: Use only hints: 1 - 3
#Difficulty Extra Hard: Use only hints 1 - 2
#Difficulty Expert: Use only hint 1

#Blackjack Rules:

#Deck is unlimited in size
#There are no jokers
#Jack/Queen/King equal to 10 each
#Ace can be either 1 or 11 based on situation

cards = [11, 2 ,3 , 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hints = {1: "There are 4 10's in the deck.", 2: "From the second draw it's pretty upward.", 3: "10 is the only recurring card in the deck.", 4: "There is a total of 13 cards in this deck."}
dealerOptions = [1, 2]
dealerChoice = 1
playAgain = True


while playAgain == True:
    print("Welcome to Blackjack, 21 is what you need to win this one!")
    print(BlackjackLogo)
    levelOfDifficulty = int(input("Choose the level of difficulty: 4 for Normal, 3 for Hard, 2 for Extra Hard, 1 for Expert."))


    for i in range(levelOfDifficulty):
        print(hints[i + 1])


    dealerCards = 0
    playerCards = 0
    dealerContinue = True

    while(dealerCards < 21 and playerCards < 21 and dealerContinue == True):
        print(f"Dealer has: {dealerCards}, you got: {playerCards}.")
        playerChoice = input('Would you like to take a card?')
        if(playerChoice == "yes"):
            nextCard = random.choice(cards)
            if(nextCard == 11 and playerCards >= 10):
                nextCard = 1

            playerCards += nextCard

            nextCard = random.choice(cards)
            if(nextCard == 11 and dealerCards >= 10):
                nextCard = 1        
            if(dealerCards < 15):
                dealerCards += nextCard
            elif(dealerCards < 21 and playerCards > dealerCards and playerCards <= 21):
                dealerCards += nextCard
        
        elif(playerChoice == "no"):
            while(dealerCards < 22 and dealerContinue == True):
                dealerChoice = random.choice(dealerOptions)
                nextCard = random.choice(cards)
                if(dealerCards >= 10 and nextCard == 11):
                    nextCard = 1
                if(dealerCards < 15):
                    dealerCards += nextCard
                elif(dealerCards < 21 and playerCards > dealerCards and playerCards <= 21):
                    dealerCards += nextCard
                else:
                    dealerContinue = False
                    
                print(f"Dealer has: {dealerCards}, you got: {playerCards}.")

        else:
            print("Wrong input!")

    if((dealerCards > 21 and playerCards > 21) or (dealerCards == playerCards)):
        winner = "it's a tie!"
    elif((dealerCards > playerCards) and (dealerCards < 22)):
        winner = "dealer wins!"
    elif(dealerCards < playerCards and playerCards > 21):
        winner = "dealer wins!"
    elif (playerCards < 22):
        winner = "player wins!"
    else:
        winner = "it's a tie!"

    print(f"Final result: dealer has: {dealerCards}, you got: {playerCards}...{winner}!")
    anotherRound = input("Would you like to play again?")
    if(anotherRound == 'no'):
        system('cls')
        print("Thanks for playing, have a nice day!")
        playAgain = False
    else:
        system('cls')

