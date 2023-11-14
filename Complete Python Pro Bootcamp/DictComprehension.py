import random as rand

students = ['David', 'Jackie', 'John', 'Belle', 'Sadie', 'Catherine', 'Melodie']

#DictComprehension over a list
studentsDict = {student:rand.randint(0,100) for student in students}
print(studentsDict)

#DictComprehension over a list based on condition
studentsPassedDict = {student:grade for (student, grade) in studentsDict.items() if grade >= 70}
print(studentsPassedDict)


