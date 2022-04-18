# Test 2 - Problem 8
def string_to_list(string):
    initial = string.split(",")
    list = []
    counter = 0
    while (counter < len(initial)):
        x, y = initial[counter].split(":")
        list.append([x,y])
        counter = counter + 1
    print(list)
    pass
string_to_list("course_name:Comp Sci-1, course_code:COMP1005/1405, term:W22, location:online")
