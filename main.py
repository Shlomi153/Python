#Created by Shlomi Kiko, inspired by the 100 day python course from Angela Yu on Udemy

#Objective:
#1) Have a question class that instantiates the object from the triviaData module
#2) Ask the user question after each question if he wants to continue until he decides to stop or you run out of questions
#3) Check if the answer is correct and output the correct result
#4) Give the user the final score out of total questions he was asked
#Use a separate class for 2 - 4

from TriviaData import triviaData
from Question import Question
from QuizBrain import QuizBrain

if __name__ == '__main__':
    questions = []

    for question in triviaData:
        questionText = question['question']
        questionAnswer = question['correct_answer']
        newQuestion = Question(questionText=questionText, correctAnswer=questionAnswer)
        questions.append(newQuestion)

    """
    for question in questions:
        print(question.question + ': ' + question.correctAnswer)
    """

    questionList = QuizBrain(questionsList=questions)

    continuePlaying = 'yes'

    while(continuePlaying == 'yes'):
        QuizBrain.NextQuestion(questionList)
        continuePlaying = input('Do you want to move to the next question?')

    finalResult = QuizBrain.FinalScore(questionList)



