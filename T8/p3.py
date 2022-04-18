import random
with open("textfile.txt", "r") as f, open("g.txt", "w") as g:
    list1 = f.readlines()
    select_string = random.choice(list1)
    g.write(select_string)
