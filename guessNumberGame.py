import random
from typing import List

def getExactMatchCount(input:str, target:str) -> str:
    result = 0
    for i in range(len(target)):
        if input[i] == target[i]:
            result += 1
    return result

def getCommonDigits(input:str, target:str) -> str:
    common_digit = list(set(input) & set(target))
    return ''.join(common_digit)


goalNumberStr = str(random.randint(100, 999))
print("goalNumberStrn : " + goalNumberStr)
guessHistory = []
while True:
    guessNumber = input('Please enter your number guessed:')
    commonChars = getCommonDigits(guessNumber, goalNumberStr)
    exactMatchCount = getExactMatchCount(guessNumber, goalNumberStr)
    if exactMatchCount == len(guessNumber) :
        print("Congratulations!")
        break
    guessHistory.append([guessNumber, commonChars, str(exactMatchCount)])
    for i in range(len(guessHistory)):
        print( str(i+1) + " Guessed number " + guessHistory[i][0] + " has perfect match count: " + guessHistory[i][2] + ", has common digits of :" + guessHistory[i][1])

