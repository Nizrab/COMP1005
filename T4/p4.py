import random
words = ["barzin","luigi","snake","peanut","hungry"]
x = random.choice(words)
s=True
while(s==True):
    try:
        letter = input("\nEnter a letter to guess: ")
        letter = letter.lower()
        if(letter in x):
            for i in range(0,len(x)) :
                if(letter == x[i]):
                    print("There are ",x.count(letter),letter+"'s")
                    break
        elif(letter.lower() == "q"):
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
            print("There are 0",letter+"'s")
        else:
            print("Please enter a value within the constraints")
            continue
    except:
        print("Please input a String value")
        continue
