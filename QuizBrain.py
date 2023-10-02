class QuizBrain:
    def __init__(self, questionsList):
        self.questionsList = questionsList
        self.questionCounter = 0
        self.userScore = 0

    def NextQuestion(self):
        self.questionCounter += 1
        currentQuestion = self.questionsList[self.questionCounter]
        userAnswer = input(f'Q{self.questionCounter}: {currentQuestion.questionText} (True/False)?')
        self.IsCorrect(userAnswer, currentQuestion.correctAnswer)

    def IsCorrect(self, userAnswer, correctAnswer):
        if(userAnswer == correctAnswer):
            print('Correct!')
            self.userScore += 1
        else:
            print('Incorrect!')
        print(f'The correct answer was: {correctAnswer}.')

    def FinalScore(self):
        return print(f'Your final score was: {self.userScore} out of {self.questionCounter} questions.')