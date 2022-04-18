x = 5
y = 2
while x != 0:
    while y <= 11:
        print("#" * y, end="")
        print("@" * x, end="")
        print("")
        x = x - 1
        y = y + 2
