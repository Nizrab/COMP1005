import random
global x
words = ["barzin","luigi","snake","peanut","hungry"]
x = random.choice(words)
checkval = True
def geuss(letter):
    s=True
    while(s==True):
        try:
            letter = letter.lower()
            if(letter in x):
                for i in range(0,len(x)) :
                    if(letter == x[i]):
                        checkval = True
                        print(x[i],end="")
                    else:
                        print("_",end="")
                s=False
            elif(letter.lower() == "quit"):
                print("The word was '"+x+"'\nGoodbye")
                s=False
                break
            elif(letter.isdigit()):
                print("Please enter a value within the constraints")
                continue
            elif(len(letter)>1):
                print("Please enter a value within the constraints")
                continue
            elif(letter not in x):
                checkval = False
                for i in range(0,len(x)) :
                    print("_",end="")
                s=False
            else:
                print("Please enter a value within the constraints")
                continue
        except:
            print("Please input a String value")
            continue

letter = input("\nEnter a letter to guess: ")
geuss(letter)
