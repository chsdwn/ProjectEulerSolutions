number = 600851475143
dividedNumber = number
dividerList = []

def checkTheNumberIsPrime(num):
    for i in range(2, int(num / 2)):
        if(num % i == 0):
            return False
            break
        else:
            return True

for i in range(2, int(number / 2)):
    if(dividedNumber % i == 0):
        if(dividedNumber > i):
            dividedNumber /= i
            dividerList.append(i)
        else:
            dividerList.append(int(dividedNumber))
            break

biggestPrimeNumber = 0
for i in range(len(dividerList)):
    if(checkTheNumberIsPrime(dividerList[i])):
        if(biggestPrimeNumber < dividerList[i]):
            biggestPrimeNumber = dividerList[i]

print("The biggest prime number that divide {} is {}".format(number, biggestPrimeNumber))