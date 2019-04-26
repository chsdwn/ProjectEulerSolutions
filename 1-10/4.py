lowest3DigitNumber = 100
biggest3DigitNumber = 999

def ReverseList(givenList):
    reversedList = []
    
    for i in range(len(givenList)):
        reversedList.append("0")

    count = 2
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
    for i in range(10):
        for j in range(10):
            number = (biggest3DigitNumber - i) * (biggest3DigitNumber - j)

            if(CheckTheNumberIsPalindrome(number)):
                print("Sayı: {} * {} = {}".format(biggest3DigitNumber, (biggest3DigitNumber - i), number))
                if(biggestPalindrome < number):
                    biggestPalindrome = number
    
    print("Biggest palindrome: {}".format(biggestPalindrome))

CalculatePalindromeNumber()