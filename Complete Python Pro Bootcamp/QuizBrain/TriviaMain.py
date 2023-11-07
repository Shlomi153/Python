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

from Question import Question
from QuizBrain import QuizBrain
from TriviaData import triviaData

def TriviaMain():
    questions = []

    for i in triviaData:
        questionText = i['question']
        correctAnswer = i['correct_answer']
        questionObj = Question(questionText=questionText, correctAnswer=correctAnswer)
        questions.append(questionObj)

    questionList = QuizBrain(questions)

    while(questionList.StillHasQuestions() == True):
        questionList.NextQuestion()

    questionList.FinalResult()



