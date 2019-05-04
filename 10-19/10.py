"""
 Problem 10:
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
"""

primeList = []
primeList.append(2)
limit = 2_000_000

i = 3
while i < limit:
    for j in range(len(primeList)):
        if i % primeList[j] == 0:
            break
        elif primeList[j] > i / 2:
            primeList.append(i)
            break
    i += 2

result = 0
for p in primeList:
    result += p

print("Sum: {}, list: {}".format(result, primeList))