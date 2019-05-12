"""
    The following iterative sequence is defined for the set of positive integers:
            n → n/2 (n is even)
            n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
            13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), 
    it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""

lengthList = []
limit = 1_000_000

index = 0

# Populate list
for i in range(0, limit + 1):
    lengthList.append([i, 0])

def numberIsEven(number):
    if number != 1:
        item[len(item) - 1] += 1
        number = int(number / 2)
        
        if number % 2 == 0:
            if number < index:
                item[len(item) - 1] += lengthList[number][1] - 1 # Minus one cause number itselft counts two times.
                number = 1
                return
            numberIsEven(number)
        else:
            numberIsOdd(number)    
    return

def numberIsOdd(number):
    if number != 1:
        item[len(item) - 1] += 1
        number *= 3
        number += 1
        numberIsEven(number)
    return

for i in range(2, limit + 1):
    item = lengthList[i]
    index = i
    
    if i % 2 == 0:
        numberIsEven(i)
    else:
        numberIsOdd(i)
    
    item[len(item) - 1] += 1

maxCount = 0
maxCountNumber = 0
for item in lengthList:
    if item[1] > maxCount:
        maxCountNumber = item[0]
        maxCount = item[1]

print("count: {}, number: {}".format(maxCount, maxCountNumber))