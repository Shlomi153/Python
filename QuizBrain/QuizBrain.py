class QuizBrain:
    def __init__(self, questions):
        self.questionList = questions
        self.score = 0
        self.counter = 0

    def StillHasQuestions(self):
        return self.counter < len(self.questionList)

    def NextQuestion(self):
        userAnswer = input(f'Q{self.counter + 1}: {self.questionList[self.counter].questionText} True/False?\n')
        correctAnswer = self.questionList[self.counter].correctAnswer
        self.IsCorrect(userAnswer, correctAnswer)
        self.counter += 1

    def IsCorrect(self, userAnswer, correctAnswer):
        if(userAnswer == correctAnswer):
            print('Correct!')
            self.score += 1
        else:
            print('Incorrect!')
        print(f'The correct answer was: {correctAnswer}.\n')

    def FinalResult(self):
        print(f'Final results: you scored {self.score} out of {self.counter} questions.\n')

