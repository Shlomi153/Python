import NatoAlphabet as alf

def PrintResult(userInput):
    for i in range(len(userInput)):
        char = userInput[i].upper()
        print(char)

        print(natoAlphDict.get(char))
    print()#Line break


natoAlphDict = alf.NatoAlphabet()

userInput = input('Write something...\n')
wordsInSentence = userInput.split(' ')

print()#Line break

for word in wordsInSentence:
    print(f'Word: {word}')
    PrintResult(word)










