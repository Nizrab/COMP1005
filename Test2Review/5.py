# Test 2 - Problem 5
def copy_even_lines(file1, file2):
    try:
        f1 = open(file1)
        f2 = open(file2)
    except FileNotFoundError:
        f1 = open(file1, "w")
        f2 = open(file2, "w")
    list = f1.readlines()
    counter = 0
    f2 = open(file2, "a")
    while (counter < len(list)):
        if ((counter % 2) == 0):
            f2.write(list[counter])
        counter = counter + 1
    f2 = open(file2, "r")
    print((f2.read()))
    f1.close()
    f2.close()
file1 = "file1.txt"
file2 = "file2.txt"
copy_even_lines(file1, file2)
