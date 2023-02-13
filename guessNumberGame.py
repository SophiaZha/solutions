import random

print("The number I am thinking of has 3 digits..")
print("")
print("'Perfect match count' is the amount of digits in your guess that are in the right position.")
print(
    "'Correct digits in guess' is the unique digits in your guess that are correct, but not necessarily in the correct position.")
print("")


def getexactmatchcount(input: str, target: str):
    result = 0
    for i in range(len(target)):
        if input[i] == target[i]:
            result += 1
    return result


def getcommondigits(input: str, target: str):
    common_digit = list(set(input) & set(target))
    return ''.join(common_digit)


getnumberstr = str(random.randint(100, 999))
print("result is " + getnumberstr)
# guessHistory = []
guess = 1
guessHistory = []
while True:
    if guess == 1:
        guessnumber = input("What is your guess?: ")
    else:
        guessnumber = input("Good try, please guess again: ")
    print("")
    commonchars = getcommondigits(guessnumber, getnumberstr)
    exactmatches = getexactmatchcount(guessnumber, getnumberstr)
    guessHistory.append([guessnumber, commonchars, str(exactmatches)])
    if exactmatches == len(guessnumber):
        print("Congragulations! You guess is corrrect. The number was " + getnumberstr + ".")
        print("It took you " + str(guess) + " tries as shown below:")
        for i in range(guess):
            print(str(i+1) + " -> " + guessHistory[i][0])
        break
    print(guessnumber + " has perfect match count: " + str(exactmatches))
    print("Correct digit(s) in guess: " + str(commonchars))
    guess += 1
