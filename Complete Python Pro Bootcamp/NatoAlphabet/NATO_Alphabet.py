#Created by Shlomi Kiko
#Goal: Receives a user's input(single word) and spells it out
#LinkedIn: https://www.linkedin.com/in/shlomikiko/

import pandas as pd

#Steps to take:
#1) import data from csv into a dataframe
#2) Create a dictionary with the letter as key and code as value from the dataframe using a dict comprehension and iterrows over the dataframe
#3) Ask the user to input a word and upper case it to make comparing easier
#4) Loop over the user input and check letters with the dictionary, if matches, add it to the new list with a list comprehension
#5) Print the new list

#Import the data into a dataframe
df_nato_alpha = pd.read_csv('./nato_phonetic_alphabet.csv')

#Connect the letters and codes row by row in a dictionary
dict_nato_alpha = {row.letter: row.code for (index, row) in df_nato_alpha.iterrows()}

#Take the user input and upper it for easy comparison
user_input = input('Please enter a word:\n').upper()

#Iterate over the user's word and compare letters between the nato dictionary and the word to save matching letter values in a new list
output_list = [dict_nato_alpha[letter] for letter in user_input]

print(output_list)
