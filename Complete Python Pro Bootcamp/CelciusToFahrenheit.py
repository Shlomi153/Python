celcius = {'Monday':32, 'Tuesday':12, 'Wednesday':26, 'Thursday':16, 'Friday':30, 'Saturday':24, 'Sunday': 42}
print('The temperatures this week in Celcius:')
printCelc = {print(day, '-', degreeInCelc) for (day, degreeInCelc) in celcius.items()}

fahrenheit = {day:((degreeCelc * 9/5) + 32) for (day, degreeCelc) in celcius.items()}

print('\nThe temperatures this week in Fahrenheit: ')
printFahrenheit = {print(k, '-', v) for (k,v) in fahrenheit.items()}