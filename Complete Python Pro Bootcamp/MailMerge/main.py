#Created by Shlomi Kiko
#Goal: Creates emails for each user in the list to be sent out
#LinkedIn: https://www.linkedin.com/in/shlomikiko/

PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt', 'r') as invited:
    names_list = invited.readlines()
    names_list = [n.strip() for n in names_list]

with open('./Input/Letters/starting_letter.txt', 'r') as template:
    start_letter = template.read()

for i in names_list:
    name = i

    with open(f'./Output/ReadyToSend/letter_for_{name}', 'w') as send_to:
        send_to.write(start_letter.replace(PLACEHOLDER, name))
