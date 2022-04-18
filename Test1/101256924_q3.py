import random
randNum = random.randint(0,9)
x = True
count = 0
print("The random digit d is",randNum)
firstNum = int(input("\nEnter a positive integer: "))
while(x == True):
    secondInput = int(input("\nEnter a positive integer: "))
    if(secondInput < 0):
        print("In total,",count,"positive integers ended with the random digit", randNum)
        break
        x=False
    elif(firstNum<secondInput):
        if(str(secondInput).endswith(str(randNum))):
            count+=1
        print("The current input",secondInput,"is greater than the previous input",firstNum)
        firstNum = secondInput
    elif(firstNum>secondInput):
        if(str(secondInput).endswith(str(randNum))):
            count+=1
        print("The current input",firstNum,"is greater than the previous input",secondInput)
        firstNum = secondInput
