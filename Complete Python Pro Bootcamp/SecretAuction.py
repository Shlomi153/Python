# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

def print_image():
   print(
   '''
                        ____________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
   '''
   )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the secret auction!")

    print_image()

    auctionDict = {}
    anyoneElse = ''
    moreParticipants = True

    while(moreParticipants):
        name = input("What is the bidder's name?\n")
        bid = float(input("Please enter your bid\n"))
        anyoneElse = input("Is there another bidder?\n").lower()

        auctionDict[name] = bid

        if(anyoneElse == "no"):
            moreParticipants = False

    maxKeyForValInDict = max(auctionDict, key=auctionDict.get)
    maxValueInDict = max(auctionDict.values())


    print("The winner of the today's auction is: {}, and the highest bid was: {}.".format(maxKeyForValInDict, maxValueInDict))







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
