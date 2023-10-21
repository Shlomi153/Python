#Created By: Shlomi Kiko
#Topic: This program takes JupyterNotebook files and converts from ipynb format to py format
#Linkedin: https://www.linkedin.com/in/shlomikiko/

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    PLACEHOLDER = '[name]'
    with open("./Input/Names/QualifiedCandidates.txt") as candidates:
        candidates = candidates.readlines()

    with open("./Input/Letters/LetterTemplate.txt") as template:
        letterTemplate = template.read()
        for name in candidates:
            strippedName = name.strip()
            newLetter = letterTemplate.replace(PLACEHOLDER, strippedName)
            with open(f"./Output/ReadyToSend/MailFor{strippedName}.txt", mode='w') as completedLetter:
                completedLetter.write(newLetter)



