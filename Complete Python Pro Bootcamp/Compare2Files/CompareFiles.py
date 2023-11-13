#Using Readlines
"""
with open('File1.csv') as file1:
    f1 = file1.readlines()
with open('File2.csv') as file2:
    f2 = file2.readlines()

f1 = [int(x) for x in f1]
f2 = [int(x) for x in f2]

valuesExistInBoth = [x for x in f1 if x in f2]
valuesExistInBoth = list(set(valuesExistInBoth))

print('First list: ', f1)
print('Second list: ', f2)
print(f'The following values exist in both lists: {valuesExistInBoth}')
"""

#Using DataFrames
"""
import pandas as pd
column = ['Num']
file1 = pd.read_csv('File1.csv', names=column)
file2 = pd.read_csv('File2.csv', names=column)

valuesExistInBoth = file1.merge(file2, how='inner', on='Num')

print(f'The following values exist in both files:\n {valuesExistInBoth}')
"""

