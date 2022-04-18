# Test 2 - Problem 2
def ceiling(x):
    y = x
    if (x >= 0):
        while (x > 1):
            if (x > 1):
                x = x - 1
        y = y + (1 - x)
    else:
        while (x < -1):
            if (x < -1):
                x = x + 1
        y = y - x
    return int(y)
ceiling(2.1)
