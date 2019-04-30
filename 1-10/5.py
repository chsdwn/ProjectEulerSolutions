# I need to optimize this code later.

resultList = []
factorsCountList = []
tempList = []

# Calculates all factors for the number and return its list
def CalculateANumbersFactors(number):
    factorsList = []

    for i in range(2, int(number / 2) + 1):
        if(number % i == 0):
            factorsList.append(i)

    if(len(factorsList) <= 0):
        factorsList.append(number)

    return factorsList

# Abbreviates factor list
def CalculateFactors(number):
    factorsList = []
    calculatedFactorsList = CalculateANumbersFactors(number)

    index = 0
    indexValue = calculatedFactorsList[index]

    while True:
        if(number % indexValue == 0):
            factorsList.append(indexValue)
            number /= indexValue
        else:
            index += 1
            if(index == len(calculatedFactorsList)):
                resultList.append(factorsList)
                return
            else:
                indexValue = calculatedFactorsList[index]
    
def CalculateResultList(number):
    for i in range(2, number + 1):
        CalculateFactors(i)

def CreateFactorsCountList(number):
    for i in range(2, number + 1):
        item = [i, 0]
        factorsCountList.append(item)

def CreateTempList(number):
    tempList.clear()
    for i in range(2, number + 1):
        tempList.append(0)

def CalculateFactorsCountList():
    number = 20
    CalculateResultList(number)
    CreateTempList(number)

    for i in range(len(resultList)):
        if(len(resultList[i]) == 1):
            factorsCountList[i][1] = 1
        elif(len(resultList[i]) >= 2):
            for j in range(len(resultList[i])):
                tempList[resultList[i][j] - 2] += 1
            for k in range(len(factorsCountList)):
                if(tempList[k] > factorsCountList[k][1]):
                    factorsCountList[k][1] = tempList[k]
            CreateTempList(number)

def CalculateResult():
    CreateFactorsCountList(20)
    CalculateFactorsCountList()
    result = 1

    for i in range(len(factorsCountList)):
        if(factorsCountList[i][1] != 0):
            for j in range(factorsCountList[i][1]):
                print("{} *= {}".format(result, factorsCountList[i][0]))
                result *= factorsCountList[i][0]

    print("Result: {}".format(result))

CalculateResult()