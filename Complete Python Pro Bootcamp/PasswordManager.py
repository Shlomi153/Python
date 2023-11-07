# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the Password Generator program!")

    numOfLetters = int(input("How many letters would you like your password to have?"))
    numOfNumbers = int(input("How many numbers should it have?"))
    numOfSymbols = int(input("And the number of symbols?"))

    passwordList = []

    for i in range(numOfLetters):
        passwordList += random.choice(letters)
    for j in range(numOfNumbers):
        passwordList += random.choice(numbers)
    for k in range(numOfSymbols):
        passwordList += random.choice(symbols)

    random.shuffle(passwordList)

    password = ""

    for char in passwordList:
        password += char
    print(f"Your new password is: {password}")



