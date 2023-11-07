#Created By: Shlomi Kiko
#Topic: This program takes JupyterNotebook files and converts from ipynb format to py format
#Linkedin: https://www.linkedin.com/in/shlomikiko/

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    PLACEHOLDER = '[name]'

    with open('./Input/Letters/LetterTemplate.txt') as template:
        template = template.read()
        with open('./Input/Names/QualifiedCandidates.txt') as qualifiedCandidates:
            qualifiedCandidates = qualifiedCandidates.readlines()
            for candidate in qualifiedCandidates:
                candidateName = candidate.strip()
                newLetter = template.replace(PLACEHOLDER, candidateName)

                with open(f'./Output/ReadyToSend/MailTo{candidateName}.txt', 'w') as mailTo:
                    mailTo.write(newLetter)



