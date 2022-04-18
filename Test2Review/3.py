# Test 2 - Problem 3
def user_words():
    list = [[],[],[],[],[],[],[],[],[],[]]
    string = ""
    while (string.lower() != "stop!"):
        string = input("Enter a string, enter 'stop!' to quit: ")
        if ((string.lower() != "stop!") & (len(string) < 10)):
            counter = 0
            match = False
            while (counter < len(list[len(string)])):
                if (list[len(string)][counter] == string):
                    match = True
                counter = counter + 1
            if (match == False):
                list[len(string)].append(string)
    return list
list = user_words()