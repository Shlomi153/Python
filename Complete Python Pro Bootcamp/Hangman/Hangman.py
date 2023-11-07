# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import HangmanPics
import ListOfWords

if __name__ == '__main__':
    print("Hi there!\nWelcome to the Hangman game, please do your very best to make sure our man stays alive :)")

    lives = 5
    display = []
    randomWord, lenRandomWord = ListOfWords.ListOfWords()

    for letter in range(lenRandomWord):
        display += "_"

    #print(f"Cheat: {randomWord}")

    while lives > 0:
        print(display)
        guess = input("Please guess a letter of the word.")

        if guess in randomWord and guess not in display:
            print("Good guess!")
            for letter in range(len(randomWord)):
                if randomWord[letter] == guess:
                    display[letter] = guess
        elif guess in randomWord and guess in display:
            print("No lives lost here, but you already guessed this one before.")
        else:
            print("Wrong guess..., one life down!")
            lives -= 1
            HangmanPics.HangmanPic(lives)
        if "_" not in display:
            break

    if lives == 0:
        print("Game over, you lose!")
    else:
        print("You won, excellent game!")


