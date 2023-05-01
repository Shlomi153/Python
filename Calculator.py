#Calculator

calculatorImg = '''
.-----------------------------.
| # Texax Instruments   TI-82 |
| .-------------------------. |
| |            ./           | |
| |            +            | |
| |. . . . . ./. . . . . . .| |
| |          / .            | |
| | X=5.2   /  .   Y=0      | |
| '-------------------------' |
| [Y=][WIN][ZOOM][TRACE][GRH] |
|                  _ [ ^ ] _  |
| [2nd][MODE][DEL]|_|     |_| |
| [ALP][XTO][STAT]   [ V ]    |
| [MATH][MAT][PGM][VARS][CLR] |
| [x-1] [SIN] [COS] [TAN] [^] |
|  [x2][ , ][ ( ][ ) ][ / ]   |
| [LOG][ 7 ][ 8 ][ 9 ] [ X ]  |
| [LN ][ 4 ][ 5 ][ 6 ] [ - ]  |
| [STO>][ 1 ][ 2 ][ 3 ][ + ]  |
| [ON][ 0 ][ . ][ (-) ][ENTR] |
| ----                        |
'-----------------------------'
'''


import math

def addition(num1, num2):
    result = float(num1 + num2)
    return result

def subtraction(num1, num2):
    result = float(num1 - num2)
    return result

def division(num1, num2):
    result = float(num1 / num2)
    return result

def multiplication(num1, num2):
    result = float(num1 * num2)
    return result

def Calculator():
    print(calculatorImg)

    continueCalculation = True
    result = 0

    operations = {
        "+":addition,
        "-":subtraction,
        "/":division,
        "*":multiplication
    }

    num1 = float(input("Please enter a number:"))

    while(continueCalculation):
        num2 = float(input("Which other number would you like to use for the calculation?"))

        for i in operations:
            print(i)

        operationChosen = input("Pick the desired operation between the two numbers:")

        calculationFunction = operations[operationChosen]
        result = calculationFunction(num1, num2)
        
        if(input(f"To continue calculating with {result} type 'y' else type 'n'.") == 'n'):
            continueCalculation = False
        else:
            num1 = result

Calculator()