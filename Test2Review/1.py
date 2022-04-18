# Test 2 - Problem 1
def aschii_caps(list):
    new = []
    counter = 0
    while (counter < len(list)):
        if (list[counter].isupper()):
            new.append(ord(list[counter]))
        counter = counter + 1
    return new
print(aschii_caps(['H', 'e', 'l', 'L', 'o', 'W', 'o', 'r', 'l', 'D']))
