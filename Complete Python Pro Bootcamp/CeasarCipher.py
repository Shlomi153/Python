# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Ceasar(message, shift, direction):
    output = ""
    shift = shift % 26
    if direction == "decrypt":
        shift *= -1
        #Shift by * -1 reverses it
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            newPosition = position + shift
            output += alphabet[newPosition]
        else:
            output += letter
    print(f"The {direction}ion is: {output}.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m","n","o","p","q","r","s"
                ,"t","u","v","w","x","y","z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m","n","o","p","q","r","s"
                ,"t","u","v","w","x","y","z"]
    play = True

    while play:
        direction = input("Choose whether you'd like to encrypt or decrypt the message.").lower()
        message = input("Please enter your message.").lower()
        shift = int(input("By how much would you like to shift?"))

        if "encrypt" in direction or "decrypt" in direction:
            Ceasar(message, shift, direction)
        else:
            print("Invalid input!")

        runAgain = input("Would you like to run the program again?")
        if runAgain == "no":
            play = False

