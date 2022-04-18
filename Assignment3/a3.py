"""
Name: Barzin Farahani
Student ID: 101256924
Date: 2022/03/13
"""
#Imports
import random
#Function to Create the deck of cards
def create_deck():
    # an intially empty deck
    deck = []
    suits = ["SP", "CL", "HR", "DM"]
    faces = []
    # creates a list of all face values
    for x in range(2,10):
        faces.append(x)
    # creates cards [s,f] and inserting them to the deck
    for s in suits:
        for f in faces:
            deck.append([s, f])
    #Returns deck
    return deck
#shuffle deck function
def shuffle(deck):
    # copies the deck, so the original deck remains same
    sdeck = deck
    random.shuffle(sdeck)
    #Returns the shuffled array
    return sdeck
#Deal Function
def deal(deck):
    #Creates the boad
    board = [[],[],[]]
    #Randomly selects a 3 x 3 of cards
    for i in range(0,3):
        board[i].append(random.choice(deck))
        board[i].append(random.choice(deck))
        board[i].append(random.choice(deck))
    #Returns the new 3 x 3board array
    return board
#Print Board function
def print_board(board):
    #Loops through board and outputs the array
    for i in board:
        print("|", end= "")
        for j in i:
            print((str(j)[1:-1]), end="|")
        print("\n")
#Update board function
def update_board(board,row,collum,newCard):
    #Inputs the new card that has been delt into the 3x3 board
    board[int(row)][int(collum)] = newCard
    for i in board:
        print("|", end= "")
        for j in i:
            print((str(j)[1:-1]), end="|")
        print("\n")
    #Returns the new board with the new item inserted
    return board
#verify match Function
def verify_matching(board,score):
    #Calls simpleSet function and checks if it returns true
    if(simpleSet(board) == True):
        score+=10
        print("Congrats!! You've got a Simple Set on the board, Score:",score)
        return True
    #Calls settt function and checks if it returns true
    elif(settt(board) == True):
        score+=15
        print("Congrats!! You've got a Set on the board, Score:",score)
        return True
    #Calls simpleRun function and checks if it returns true
    elif(simpleRun(board) == True):
        score+=20
        print("Congrats!! You've got a Simple Run on the board, Score:",score)
        return True
    #Calls run function and checks if it returns true
    elif(run(board) == True):
        score+=25
        print("Congrats!! You've got a Run on the board, Score:",score)
        return True
    #Returns False if none of the earlier if statments hit
    else:
        return False
#Simple set function
def simpleSet(board):
    #Checks Suits top to bottom
    if(board[0][0][0] == board[1][0][0] and board[1][0][0] == board[2][0][0]):
        return True
    elif(board[0][1][0] == board[1][1][0] and board[1][1][0] == board[2][1][0]):
        return True
    elif(board[0][2][0] == board[1][2][0] and board[1][2][0] == board[2][2][0]):
        return True
    #Checking Suits side to side
    elif(board[0][0][0] == board[0][1][0] and board[0][1][0] == board[0][2][0]):
        return True
    elif(board[1][0][0] == board[1][1][0] and board[1][1][0] == board[1][2][0]):
        return True
    elif(board[2][0][0] == board[2][1][0] and board[2][1][0] == board[2][2][0]):
        return True
#Set function
def settt(board):
    #Top Bottoem Check for matching number
    if(board[0][0][1] == board[1][0][1] and board[1][0][1] == board[2][0][1]):
        return True
    elif(board[0][1][1] == board[1][1][1] and board[1][1][1] == board[2][1][1]):
        return True
    elif(board[0][2][1] == board[1][2][1] and board[1][2][1] == board[2][2][1]):
        return True
    #side to side for matching number
    elif(board[0][0][1] == board[0][1][1] and board[0][1][1] == board[0][2][1]):
        return True
    elif(board[1][0][1] == board[1][1][1] and board[1][1][1] == board[1][2][1]):
        return True
    elif(board[2][0][1] == board[2][1][1] and board[2][1][1] == board[2][2][1]):
        return True
#simpleRun function
def simpleRun(board):
    #Top Bottoem Check for number increasing by 1
    if(int(board[0][0][1])+1 == board[1][0][1] and int(board[1][0][1])+1 == board[2][0][1]):
        return True
    elif(int(board[0][1][1])+1 == board[1][1][1] and int(board[1][1][1])+1 == board[2][1][1]):
        return True
    elif(int(board[0][2][1])+1 == board[1][2][1] and int(board[1][2][1])+1 == board[2][2][1]):
        return True
    #side to side for number increasing by 1
    elif(int(board[0][0][1])+1 == board[0][1][1] and int(board[0][1][1])+1 == board[0][2][1]):
        return True
    elif(int(board[1][0][1])+1 == board[1][1][1] and int(board[1][1][1])+1 == board[1][2][1]):
        return True
    elif(int(board[2][0][1])+1 == board[2][1][1] and int(board[2][1][1])+1 ==board[2][2][1]):
        return True
#run function
def run(board):
    #checking from top left to bottom right
    if(board[0][0][0] == board[1][1][0] and board[1][1][0] == board[2][2][0] and int(board[0][0][1])+1 == board[1][1][1] and int(board[1][1][1])+1 == board[2][2][1]):
        return True
    #Checking from the top right to the bottom left
    elif(board[0][2][0] == board[1][1][0] and board[1][1][0] == board[2][0][0] and int(board[0][2][1])+1 == board[1][1][1] and int(board[1][1][1])+1 == board[0][2][1]):
        return True
#Game function
def game(boleoean,score):
    #if true bool is passed through return nothing
    if(boleoean == True):
        print("")
    #if false return lose statment
    elif(boleoean == False):
        print("Sorry, no match on the board. Score:",score)
#Main Function
def main():
    lvl = 0
    score = 0
    print("Welcome to the game!\n")
    deck = create_deck()
    #returns shuffled deck of cards
    shuffDeck = shuffle(deck)
    #Returns board with 3x3 table/output
    dealz = deal(shuffDeck)
    #prints out the table
    print_board(dealz)
    #Gets a new card when user selects deal then will ask where the user wants to place it
    x = True
    #card amount val
    cardsLeft = len(deck) - 9
    #While loop containing the game
    while(x == True):
        print("Cards left to play: ", cardsLeft)
        #if cars are left continue
        if(cardsLeft>0):
            #takes the input for deal or done
            print("Score:",score, "Deal or Done?: ", end='')
            dealInput = input()
            #lowers input then compares
            if(dealInput.lower() == 'deal'):
                lvl+=1
                cardsLeft-=1
                #Randomly slects a card from the array
                newCard = random.choice(shuffDeck)
                #loop for replacing the card
                while(True):
                    print("New card: ",newCard,", enter location to replace card <row col>:", end= ' ')
                    #Try catch for input validation
                    try:
                        userInput = input()
                        #gets row and collum fom user
                        row = userInput[0]
                        collum = userInput[1]
                        if(len(userInput)>2):
                            print("")
                            continue
                        else:
                            #Calls update board function with new card and spot
                            up = update_board(dealz,row,collum,newCard)
                            score-=1
                            break
                    except:
                        print("Invalid input, please try again.\n")
            #When user selects done
            elif(dealInput.lower() == 'done'):
                #Verifys if user won or not
                #also checks wiether it was the first move or not
                if(lvl!=0):
                    #if not the first move uses updated boared
                    v = verify_matching(up,score)
                    game(v,score)
                    x = False
                else:
                    #If the first move uses original board'
                    v = verify_matching(dealz,score)
                    game(v,score)
                    x = False
            #Input validation
            else:
                print("Invalid choice.\n")
                continue
        #When the user runs out of cards
        else:
            print("Sorry, You ran out of cards. Score:",score)
            x = False
            break

if __name__ == "__main__":
    main()
