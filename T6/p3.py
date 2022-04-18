import random
global words
words = []
def word_selection(letter):
    s=True
    while(s==True):
        if validate(letter) == "Invalid":
            print("Invalid input, please enter a valid input.")
            return
        elif(letter.isalpha):
            words.append(letter)
            break

def validate (a):
    if a.isdigit():
        return "Invalid"
    else:
        return a

def main():
    while True:
        letter = input("Enter a word (or ‘q’ to quit): ")
        if letter.lower() == "q":
            if not words:
                print("Sorry the Array is empty")

            else:
                print("The selected word is "+random.choice(words))

            break
        else:
            word_selection(letter)

if __name__ == "__main__":
    main()
