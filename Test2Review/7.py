# Test 2 - Problem 7
def mutate_list(list):
    new = []
    counter = 0
    while(counter < len(list)):
        new.append(list[counter])
        counter = counter + 1
    counter = 0
    while (counter < len(new)):
        while (len(new[counter]) < 5):
            new[counter].append(0)
        counter = counter + 1
    dim0 = 0
    dim1 = 0
    while (dim0 < len(new)):
        while (dim1 < len(new[dim0])):
            if ((new[dim0][dim1] % 2) == 0):
                new[dim0][dim1] = int((new[dim0][dim1] / 2))
            elif (((new[dim0][dim1] % 2) == 1) & (new[dim0][dim1] < 10)):
                new[dim0][dim1] = (new[dim0][dim1] * 10)
            dim1 = dim1 + 1
        dim1 = 0
        dim0 = dim0 + 1
    return new
print(mutate_list([[8,5,7,2],[13,12,9,17,5],[10,20],[1,2,3,4,5,6]]))
