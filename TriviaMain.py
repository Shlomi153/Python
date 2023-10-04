#Created by Shlomi Kiko, inspired by the 100 day python course from Angela Yu on Udemy

#Objective:
#1) Have a question class that instantiates the object from the triviaData module
#2) Ask the user question after each question if he wants to continue until he decides to stop or you run out of questions
#3) Check if the answer is correct and output the correct result
#4) Give the user the final score out of total questions he was asked
#Use a separate class for 2 - 4

#The files related to this one are:
#1) Question.py
#2) QuizBrain
#3) TriviaData

from TriviaData import triviaData
from Question import Question
from QuizBrain import QuizBrain

def TriviaMain():
    questions = []

    for question in triviaData:
        questionText = question['question']
        questionAnswer = question['correct_answer']
        questionObject = Question(questionText=questionText, correctAnswer=questionAnswer)
        questions.append(questionObject)

    continuePlaying = 'Yes'

    questionsList = QuizBrain(questions)

    print('Welcome to the lovely Quiz of the day!\nLet us begin:\n')

    while (questionsList.StillHasQuestions() == True):
        questionsList.NextQuestion()

    questionsList.FinalResult()



