#Number guessing game, idea is to guess a number between a range.
#Two levels of difficulty with the harder level providing double the attempts to guess

import random

POSSIBLE_ATTEMPS_EASY = 10
POSSIBLE_ATTEMPS_HARD = 5
MIN_NUM_RANGE = 0
MAX_NUM_RANGE = 100

winningNum = random.randrange(MIN_NUM_RANGE, MAX_NUM_RANGE)
countNumAttemps = 0

logo = '''
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  
 aa,    ,88                                             
  "Y8bbdP"      
'''


#Progam logic that gets user input and gives him attempts based on level of difficulty
def UserGuess(difficultyLevelChosen):
    if(difficultyLevelChosen == 1):
        countNumAttemps = POSSIBLE_ATTEMPS_EASY
        levelAttemps = POSSIBLE_ATTEMPS_EASY
    elif(difficultyLevelChosen == 2):
        countNumAttemps = POSSIBLE_ATTEMPS_HARD
        levelAttemps = POSSIBLE_ATTEMPS_HARD
    else:
        print("Invalid input, unknown level difficulty!")
        return

    for i in range(levelAttemps):
        countNumAttemps -=1

        numChosen = int(input(f"Please choose a number between {MIN_NUM_RANGE} and {MAX_NUM_RANGE}:"))
        
        while(numChosen > MAX_NUM_RANGE or numChosen < MIN_NUM_RANGE):
            print(f"Number out of range, please pick a number between {MIN_NUM_RANGE} and {MAX_NUM_RANGE}:")
            numChosen = int(input(f"Please choose a number between {MIN_NUM_RANGE} and {MAX_NUM_RANGE}:")) 

        if(numChosen == winningNum):
            print(f"Amazing, you got it right!\nThe winning number is: {winningNum}")
            break
        else:
            if(countNumAttemps == 0):
                break
            print(f"Too bad, wasn't the number we were thinking of, you can try {countNumAttemps} more times to guess it.")

            if(numChosen < winningNum):
                print("Was a bit too low...")
            else:
                print("Was a bit too high...")
    
    if(numChosen != winningNum):
        print("Sorry, you lose this one, better luck next time!")



#Begins here
print(logo)
difficultyLevelChosen = int(input("Please choose the level you'd like to play: \n1 for easy\n2 for hard\n"))
UserGuess(difficultyLevelChosen)

    







