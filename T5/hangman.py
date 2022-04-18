#Robert Hale (101236120), Barzin Farahani (101256924), Daniel Groleau (101247083), Alem Gebeyehu (101169359), Luke Goedvolk (101121639), Jonathan Elliot (101235435)
#Tutorial 5, Problems 1 - 4

from json.tool import main
import random

#global variables
guesses = 0
words = ["barzin","luigi","snake","peanut","hungry"]
x = random.choice(words)

#hangman print function (problem 1)
def print_hangman():
    if guesses == 1:
        print ("\n O")
    elif guesses == 2:
        print ("\n O\n |")
    elif guesses == 3:
        print ("\n O\n\\|\n |")
    elif guesses == 4:
        print ("\n O\n\\|/\n |")
    elif guesses == 5:
        print ("\n O\n\\|/\n |\n/")
    elif guesses == 6:
        print ("\n O\n\\|/\n |\n/ \\")
    else:
        print()
    return

#guess function (problem 2)
def guess(letter):
    global guesses
    while(True): 
        if validate(letter) == "Invalid":
            print("Invalid input, please enter a valid input.")
            return     
        letter = letter.lower()
        if(letter in x):
            for i in range(0,len(x)):
                if(letter == x[i]):
                    print(x[i],end="") 
                else:
                    print("_",end="")
            print_hangman()
            return True
        else:
            for i in range(0,len(x)):
                print("_",end="") 
            guesses += 1 
            print_hangman() 
        return False

#validate option for error checking (problem 3)
def validate (a):
    if len(a) > 1 or a.isdigit():
        return "Invalid"
    else:
        return a

#main function (problem 4)
def main():
    while True:
        user_guess = input("Guess a letter: ")
        if user_guess == "quit":
            print("The word was: "+ x + ".")
            break
        user_guess = guess(user_guess)
        if user_guess == True:
            pass
        elif user_guess == False:
            if guesses == 6:
                print("You lose.\nThe word was: "+ x + ".")
                break

if __name__ == "__main__":
    main()
