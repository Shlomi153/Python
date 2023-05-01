# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def IsPrimeNumber(num):
    isPrimeNum = True

    for i in range(2, num):
        if num % i == 0:
            isPrimeNum = False

    return isPrimeNum

def PrintPrimeNumbers(num):
    for i in range(num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = int(input("Enter a number:\n"))
    result = IsPrimeNumber(num)
    PrintPrimeNumbers(num)
    print(f"Is the number a prime number?\n{result}")

