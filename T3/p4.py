s=True
while(s==True):
    try:
        x = int(input("\nPlease enter a number between 1 - 6: "))
        if(x>=1 and x<=6):
            print("Correct Value")
            s=False
        else:
            print("Please enter a value within the constraints")
            continue
    except:
        print("Please input a integer value")
        continue
