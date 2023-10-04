class QuizBrain:
    def __init__(self, questionsList):
        self.questionsList = questionsList
        self.score = 0
        self.counter = 0

    def NextQuestion(self):
        userAnswer = input(f'Q{self.counter + 1}: {self.questionsList[self.counter].question} True/False?.\n').lower()
        correctAnswer = self.questionsList[self.counter].correctAnswer
        self.counter += 1
        self.IsCorrect(userAnswer, correctAnswer)

    def StillHasQuestions(self):
        return self.counter < len(self.questionsList)

    def IsCorrect(self, userAnswer, correctAnswer):
        if(userAnswer.lower() == correctAnswer.lower()):
            print('Correct!')
            self.score += 1
        else:
            print('Wrong answer!')
        print(f'The correct answer was: {correctAnswer}.\n')

    def FinalResult(self):
        print(f'Your final score is: {self.score} out of {self.counter} questions.\n')
