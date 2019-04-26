num1 = 1
num2 = 1

total = 0

while(True):
    num3 = num1 + num2
    
    if(num3 < 4000000):
        #Adds even counts to total
        if(num3 % 2 == 0):
            total += num3
    else:
        print("Total: {}".format(total))
        break

    num1 = num2
    num2 = num3