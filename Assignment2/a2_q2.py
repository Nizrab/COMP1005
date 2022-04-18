"""
Name: Barzin Farahani
Student ID: 101256924
Date: 2022/02/22
"""
#Imports Random
import random
#Menu Function which takes in varibles: level and userName
def menu(level,userName):
    #If level 1 Menu output
    if(level == 1):
        print("\nWelcome to the game,",userName+"! Want to find some secret treasures? Let's begin.")
        print("\nYou can choose a door to get the treasures hidden behind it\nBut you must also collect a token from the magic wheel to open that door.\nCheck how much you can win and the token you need to open a door.\nIf you win this level, you'll get 1 x the value of the treasure.\nBut if you lose, 1 x the value of the treasure will be taken away from you.\n------------------------- Level-1 -----------------------------------")
        print("Doors\tTreasures' value\tToken type\n[1] Door-1\t$100.00\t\tSilver\n[2] Door-2\t$200.00\t\tGold\n[3] Door-3\t$300.00\t\tDiamond\n----------------------------------------------------------------------\nWhich door do you want to choose? Type [1, 2, or 3]. To quit the game enter 'q'.")
    #If level 2 Menu output
    elif(level == 2):
        print("\nIf you win this level, you'll get 2 x the value of the treasure.\nBut if you lose, 2 x the value of the treasure will be taken away from you. \n------------------------- Level-2 -----------------------------------")
        print("Doors\tTreasures' value\tToken type\n[1] Door-1\t$200.00\t\tSilver\n[2] Door-2\t$400.00\t\tGold\n[3] Door-3\t600.00\t\tDiamond\n----------------------------------------------------------------------\nWhich door do you want to choose? Type [1, 2, or 3]. To quit the game enter 'q'.")
    #If level 3 Menu output
    elif(level == 3):
        print("Level 3")
        print("\nIf you win this level, you'll get 3 x the value of the treasure.\nBut if you lose, 3 x the value of the treasure will be taken away from you.\n------------------------- Level-3 -----------------------------------")
        print("Doors\tTreasures' value\tToken type\n[1] Door-1\t$300.00\t\tSilver\n[2] Door-2\t$600.00\t\tGold\n[3] Door-3\t$900.00\t\tDiamond\n----------------------------------------------------------------------\nWhich door do you want to choose? Type [1, 2, or 3]. To quit the game enter 'q'.")
#Game Function
def game():
    #Member varibles
    level = 1
    s = True
    #get users name
    userName = input("Hey gamer, what's your preferred name?\n>> ")
    #While loop for game
    while(s==True):
        #Call menu function and input requird values
        menu(level,userName)
        #Select a random number
        randNum = random.randint(0,100)
        #try catch for input validation
        try:
            #User inputs door selection
            userDoorSelection = input(">> ")
            #If user slects door 1
            if(userDoorSelection.isdigit() and int(userDoorSelection) == 1):
                while(True):
                    #User selects if they want to change their door
                    print("Do you want to change your decision and choose another door? Enter 'Yes'/'No'")
                    userRealDoorSelection = input(">> ")
                    #if yes reselect
                    if(userRealDoorSelection.lower() == 'yes'):
                        print("Which door do you want to choose? Type [1, 2, or 3]")
                        break
                    #if no continue
                    elif(userRealDoorSelection.lower() == 'no'):
                        #if randNum is <60 silver coin output
                        if(randNum<=60):
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-1. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Silver token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $100.00\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        #if randNum is <90 gold coin output
                        elif(randNum<=90):
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-1. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Gold token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $100.00\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        #else Dimond coin output
                        else:
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-1. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Dimond token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $100.00\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        break
                    #input validation
                    else:
                        print("Invalid input, please try again.")
                        continue
            #If user slects door 2
            elif(userDoorSelection.isdigit() and int(userDoorSelection) == 2):
                while(True):
                    #User selects if they want to change their door
                    print("Do you want to change your decision and choose another door? Enter 'Yes'/'No'")
                    userRealDoorSelection = input(">> ")
                    #If yes user reselects door
                    if(userRealDoorSelection.lower() == 'yes'):
                        print("Which door do you want to choose? Type [1, 2, or 3]")
                        break
                    #If not continue
                    elif(userRealDoorSelection.lower() == 'no'):
                        #if randNum is <60 silver coin output
                        if(randNum<=60):
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-2. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Silver token ("+str(randNum)+"%)\n\nBad luck.. can't open Door-2 with a silver token, you didn't win anything.\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        #if randNum is <90 silver coin output
                        elif(randNum<=90):
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-2. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Gold token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $200.00\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        #Else dimond coin output
                        else:
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-2. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Dimond token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $200.00\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        break
                    #input validation
                    else:
                        print("Invalid input, please try again.")
                        continue
            #If user slects door 3
            elif(userDoorSelection.isdigit() and int(userDoorSelection) == 3):
                while(True):
                    #User selects if they want to change their door
                    print("Do you want to change your decision and choose another door? Enter 'Yes'/'No'")
                    userRealDoorSelection = input(">> ")
                    #If yes user reselects door
                    if(userRealDoorSelection.lower() == 'yes'):
                        print("Which door do you want to choose? Type [1, 2, or 3]")
                        break
                    #If not continue
                    elif(userRealDoorSelection.lower() == 'no'):
                        #if randNum is <60 silver coin output
                        if(randNum<=60):
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-3. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Silver token ("+str(randNum)+"%)\n\nBad luck.. can't open Door-3 with a silver token, you didn't win anything.\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        #if randNum is <90 gold coin output
                        elif(randNum<=90):
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-3. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Gold token ("+str(randNum)+"%)\n\nBad luck.. can't open Door-3 with a gold token, you didn't win anything.\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        #else Dimond coin output
                        else:
                            #increases level and outputs if user won or not
                            level += 1
                            print(userName+", you have selected Door-3. Please spin the magic wheel to collect your token.\n...... (drum roll) .... you've got a Dimond token ("+str(randNum)+"%)\n\nCongrats!! You've won the hidden treasure worth $300.00\nThanks for playing!")
                            if(level>3):
                                print("Congrats you have completed all the levels")
                                s=False
                            else:
                                #Loop to see if user wants to play again
                                while(True):
                                    print("Do you want to play the next level (Level-",level,") (enter 'Yes'/'No')?")
                                    again = input(">> ")
                                    #If yes break and return to menu
                                    if(again.lower() == 'yes'):
                                        break
                                    #If no turn f contidtion  to false and quit
                                    elif(again.lower() == 'no'):
                                        print("You've decided to quit..\nThanks for playing! ")
                                        s=False
                                        break
                                    #input validation
                                    else:
                                        print("Invalid input, please try again.")
                                        continue
                        break
                    #input validation
                    else:
                        print("Invalid input, please try again.")
                        continue
            #If user inputs q to quit
            elif(userDoorSelection.lower() == "q"):
                print("\nGoodbye")
                s=False
                break
            #input validation
            elif(int(userDoorSelection)<=0 or int(userDoorSelection)>3 ):
                print("Invalid input, please enter a single digit between 1 and 3.")
                continue
        #input validation
        except:
            print("Invalid input, please try again.")

#Run game Function
game()
