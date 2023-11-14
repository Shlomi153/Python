#Splits a sentence written by the user into words and shows the number of characters per word
sentence = input('Write something\n')

wordsList = sentence.split()
totalLettersPerWord = {word:len(word) for word in wordsList}

print(totalLettersPerWord)