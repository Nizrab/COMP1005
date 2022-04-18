def my_strs(word):
    print(word.upper())
    length = len(word)%2
    if length == 0:
        print("\n'"+word+"' has an even length\n")
    else:
        print("\n'"+word+"' has an odd length\n")

    for i in range(len(word)):
        print(word[i])
    for i in range(len(word)):
        print("\nhello")

my_strs("Good luck!")
