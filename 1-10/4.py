"""
Problem 4:
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
"""

lowest3DigitNumber = 100
biggest3DigitNumber = 999

def ReverseList(givenList):
    reversedList = []
    
    for i in range(len(givenList)):
        reversedList.append("0")

    count = len(givenList) - 1
    for j in range(len(givenList)):
        reversedList[count] = givenList[j]
        count -= 1

    return reversedList
        
def CheckTheNumberIsPalindrome(number):
    numberDigits = list(str(number))
    leftSide = []
    rightSide = []

    for i in range(len(numberDigits)):
        if(i < int((len(numberDigits) / 2))):
            leftSide.append(numberDigits[i])
        else:
            rightSide.append(numberDigits[i])
    
    rightSide = ReverseList(rightSide)

    if(leftSide == rightSide):
        return True
    else:
        return False

def CalculatePalindromeNumber():
    biggestPalindrome = 0
    for i in range(100):
        for j in range(100):
            number = (biggest3DigitNumber - i) * (biggest3DigitNumber - j)

            if(CheckTheNumberIsPalindrome(number)):
                print("{} = {} * {}".format(number, (biggest3DigitNumber - i), (biggest3DigitNumber - j)))
                if(biggestPalindrome < number):
                    biggestPalindrome = number
    
    print("Biggest palindrome: {}".format(biggestPalindrome))

CalculatePalindromeNumber()