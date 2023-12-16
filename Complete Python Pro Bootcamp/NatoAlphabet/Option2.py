import pandas as pd

#Read CSV file into a dictionary
df_natoFile = pd.read_csv(r'D:\Python Projects\Angela Yu - Course\NatoAlphabet\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv')
#print(df_natoFile)

#Put the data into a dictionary, index is the key, row is the value
dictNato = {row.letter: row.code for (index, row) in df_natoFile.iterrows()}

#(dictNato)

#Get user input and put it in a list
userInput = input('Write something...\n')
wordsInSentence = userInput.split(' ')

for i in range(len(wordsInSentence)):
    print(f'Word: {wordsInSentence[i]}')
    charsInWord = [dictNato.get(letter, 'Character not in Nato Alphabet!') for letter in wordsInSentence[i].upper()]#Upper to compare it correctly with dictNato
    print(charsInWord)
