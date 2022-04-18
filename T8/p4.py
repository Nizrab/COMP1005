from json.tool import main
import random

guesses = 0
guess_list = []
words = []
try:
    open("output.txt","x")
except:
    print("Welcome Back!")

o = open("output.txt", "w")

with open("samplefile_t8.txt", "r") as f:
    words = f.readlines()

word_selected = random.choice(words)
f.close()

def print_hangman():
    txt = ""
    if guesses == 1:
        txt ="\n O"
    elif guesses == 2:
        txt ="\n O\n |"
    elif guesses == 3:
        txt ="\n O\n\\|\n |"
    elif guesses == 4:
        txt ="\n O\n\\|/\n |"
    elif guesses == 5:
        txt ="\n O\n\\|/\n |\n/"
    elif guesses == 6:
        txt ="\n O\n\\|/\n |\n/ \\"
    return txt



def guess(letter):
    global guesses
    global guess_list
    guess_count = 0
    global word_selected
    while True:
        if validate(letter) == "Invalid":
            print("Invalid input, please enter a valid input.")
            return
        for entry in guess_list:
            if entry[0] == letter:
                print("This letter has already been guessed.")
                entry[1] += 1
            else:
                guess_list.append([user_guess, 1])
        if(letter in word_selected):
            for i in range(0, len(word_selected)):
                if(letter == word_selected[i]):
                    print(word_selected[i], end="")
                else:
                    print("_", end="")
            print(print_hangman())
            return True
        else:
            for i in range(0, len(word_selected)):
                print("_", end="")
            guesses += 1
            print(print_hangman())
        return False


def validate(user_guess):
    if not user_guess.isalpha() or len(user_guess) != 1:
        return "Invalid"
    else:
        return user_guess


def main():
    while True:
        if guesses == 6:
            break
        user_guess = input("Guess a letter: ").lower()
        if user_guess == "quit":
            print("The word was: " + x + ".")
            break
        guess(user_guess)
        if(all(item in guess_list for item in word_selected)== True):
           o.write(x)
           o.write(print_hangman())
           print("You win. \nThe word was: "+x+".")
           o.write("You win. \nThe word was: "+x+".")

        elif user_guess == True:
           pass
        elif user_guess == False:
          if guesses == 6:


            o.write(x)
            o.write(print_hangman())
            print("You lose.\nThe word was: "+ x + ".")
            o.write("You lose.\nThe word was: "+ x + ".")
            break


if __name__ == '__main__':
    main()
