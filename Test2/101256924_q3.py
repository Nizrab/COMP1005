def analyze(userInput):
    count1 = 0
    count2 = 0
    #Part1
    for i in userInput:
        if(i.isupper()):
            count1=count1+1
    print("The input string has ",count1,"uppercase letters in it.\n")
    #Part2
    if(userInput[0] == 'h' and userInput[len(userInput)-1] == 'g'):
        print("The input string starts with 'h' and ends with 'g'.\n")
    else:
        print("The input string does not start with 'h' and end with 'g'.\n")
    #Part3
    for i in userInput.lower().split():
        if 'a' in i:
            count2=count2+1
    print("The input string has",count2,"words that have the letter 'a' in it.")

def main():
    myStr="AAh! it'S bEaUTiFUl OutSide"
    analyze(myStr)

if __name__ == "__main__":
    main()
