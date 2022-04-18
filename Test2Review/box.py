# Test 2 - Problem 9
def read_file(file):
    try:
        f = open(file)
    except FileNotFoundError:
        f = open(file, "w")
    f = open(file, "r")
    initial = (f.read()).split()
    counter = 0
    while (counter < len(initial)):
        initial[counter] = int(initial[counter].strip(","))
        counter = counter + 1
    list = []
    counter = 0
    while (counter < (len(initial))):
        list.append([initial[counter], initial[counter + 1],initial[counter + 2]])
        counter = counter + 3
    f.close
    return list
def max_volume(list):
    volume = 0
    counter = 0
    while (counter < len(list)):
        if ((list[counter][0] * list[counter][1] * list[counter][2]) > volume):
            volume = (list[counter][0] * list[counter][1] * list[counter][2])
        counter = counter + 1
    return volume
def main():
    file = ""
    file = input("File: ")    #default file is "file.csv"
    list = read_file(file)
    volume = max_volume(list)
    print(volume)
if __name__ == '__main__':
    main()
