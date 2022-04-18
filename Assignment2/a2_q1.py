"""
Name: Barzin Farahani
Student ID: 101256924
Date: 2022/02/22
"""
#Imports random lib
import random
#Function for the game
def game():
    s=True
    #Gets users name
    userName = input("Hey gamer, what's your preferred name?\n>> ")
    #Menu gets printed
    print("Welcome to the game,",userName+"! Want to find some secret treasures? Let's begin.")
    print("\nYou can choose a door to get the treasures hidden behind it\nBut you must also collect a token from the magic wheel to open that door.\nCheck how much you can win and the token you need to open a door.\n----------------------------------------------------------------------")
    print("Doors\tTreasures' value\tToken type\n[1] Door-1\t$100.00\t\tSilver\n[2] Door-2\t$200.00\t\tGold\n[3] Door-3\t$300.00\t\tDiamond\n\nWhich door do you want to choose? Type [1, 2, or 3]. To quit the game enter 'q'.")
    #While loop for the game
    while(s==True):
        #Selecting random number
        randNum = random.randint(0,100)
        #try catch for user input
        try:
            #User inputs door selection
            userDoorSelection = input(">> ")
            #If user selects door 1
            if(userDoorSelection.isdigit() and int(userDoorSelection) == 1):
                #Loop for if user wants to swich doors
                while(True):
                    #User slects new door or keeeps the one picked
                    print("Do you want to change your decision and choose another door? Enter 'Yes'/'No'")
                    userRealDoorSelection = input(">> ")
                    #If yes reslect door
                    if(userRealDoorSelection.lower() == 'yes'):
                        print("Which door do you want to choose? Type [1, 2, or 3]")
                        break
                    #If not user keeps first selection then will output if they won or not
                    elif(userRealDoorSelection.lower() == 'no'):
                        if(randNum<=60):
                            #Output for Silver Coin
                            print(userName+", you have selected Door-1. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Silver token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $100.00\nThanks for playing!")
                            s=False
                        elif(randNum<=90):
                            #Output for Gold Coin
                            print(userName+", you have selected Door-1. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Gold token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $100.00\nThanks for playing!")
                            s=False
                        else:
                            #Output for Dimond Coin
                            print(userName+", you have selected Door-1. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Dimond token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $100.00\nThanks for playing!")
                            s=False
                        break
                    #Checks for valid inputs
                    else:
                        print("Invalid input, please try again.")
                        continue
            #If user selects door 2
            elif(userDoorSelection.isdigit() and int(userDoorSelection) == 2):
                #Loop for if user wants to swich doors
                while(True):
                    #User slects new door or keeeps the one picked
                    print("Do you want to change your decision and choose another door? Enter 'Yes'/'No'")
                    userRealDoorSelection = input(">> ")
                    #If yes reslect door
                    if(userRealDoorSelection.lower() == 'yes'):
                        print("Which door do you want to choose? Type [1, 2, or 3]")
                        break
                    #If not user keeps first selection then will output if they won or not
                    elif(userRealDoorSelection.lower() == 'no'):
                        if(randNum<=60):
                            #Output for Silver Coin
                            print(userName+", you have selected Door-2. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Silver token ("+str(randNum)+"%)\n\nBad luck.. can't open Door-2 with a silver token, you didn't win anything.\nThanks for playing!")
                            s=False
                        elif(randNum<=90):
                            #Output for Gold Coin
                            print(userName+", you have selected Door-2. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Gold token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $200.00\nThanks for playing!")
                            s=False
                        else:
                            #Output for Dimond Coin
                            print(userName+", you have selected Door-2. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Dimond token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $200.00\nThanks for playing!")
                            s=False
                        break
                    #Checks for valid inputs
                    else:
                        print("Invalid input, please try again.")
                        continue
            #If user selects door 3
            elif(userDoorSelection.isdigit() and int(userDoorSelection) == 3):
                #Loop for if user wants to swich doors
                while(True):
                    #User slects new door or keeeps the one picked
                    print("Do you want to change your decision and choose another door? Enter 'Yes'/'No'")
                    userRealDoorSelection = input(">> ")
                    #If yes reslect door
                    if(userRealDoorSelection.lower() == 'yes'):
                        print("Which door do you want to choose? Type [1, 2, or 3]")
                        break
                    #If not user keeps first selection then will output if they won or not
                    elif(userRealDoorSelection.lower() == 'no'):
                        if(randNum<=60):
                            #Output for Silver Coin
                            print(userName+", you have selected Door-3. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Silver token ("+str(randNum)+"%)\n\nBad luck.. can't open Door-3 with a silver token, you didn't win anything.\nThanks for playing!")
                            s=False
                        elif(randNum<=90):
                            #Output for Gold Coin
                            print(userName+", you have selected Door-3. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Gold token ("+str(randNum)+"%)\n\nBad luck.. can't open Door-3 with a gold token, you didn't win anything.\nThanks for playing!")
                            s=False
                        else:
                            #Output for Dimond Coin
                            print(userName+", you have selected Door-3. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Dimond token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $300.00\nThanks for playing!")
                            s=False
                        break
                    #Checks for valid inputs
                    else:
                        print("Invalid input, please try again.")
                        continue
            #If user enters q to quit
            elif(userDoorSelection.lower() == "q"):
                print("\nGoodbye")
                s=False
                break
            #Input validation makin sure that its between 1-3
            elif(int(userDoorSelection)<=0 or int(userDoorSelection)>3 ):
                print("Invalid input, please enter a single digit between 1 and 3.")
                continue
        #Eception to catch invalid inputs
        except:
            print("Invalid input, please try again.")

#Running the Function
game()
