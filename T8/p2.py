def less_than_age(file1,compare):
    arrAnimal = []
    try:
        f = open(file1,"r")
    except FileNotFoundError:
        print("FileNotFoundError")
    texts = f.readlines()
    for line in texts:
        line = line.strip(',"\n')
        line = line.split(",")
        if(int(line[1])<compare):
            arrAnimal.append(line[0])
    print(arrAnimal)
    f.close()

def main():
    file="samplefile_t8.txt"
    less_than_age(file,4)

if __name__ == "__main__":
    main()
