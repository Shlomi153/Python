def NatoAlphabet():
    with open(r'D:\Python Projects\Angela Yu - Course\NatoAlphabet\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv') as file:
        natoAlphabet = file.readlines()
        # Remove header
        natoAlphabet.remove(natoAlphabet[0])
        #Create a dictionary out of the values to easier reach them
        natoDict = {x[0]: x[2:-1] for x in natoAlphabet}#Remove the linebreak for each value
        return natoDict