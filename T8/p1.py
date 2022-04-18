#Robert Hale (101236120), Barzin Farahani (101256924), Daniel Groleau (101247083), Alem Gebeyehu (101169359), Luke Goedvolk (101121639), Jonathan Elliot (101235435)
#Tutorial 8 - Problem 1

#filereader function, takes 2 arguments, returns nothing
def filereader(file, fileIt):
    #initialized variables to be used in the function
    fileList = []
    fileDisplay = []
    it = fileIt
    count = 0
    #opens and reads 'samplefile_t8.txt'
    f = open(file, 'r')
    x = f.readlines()
    #for-loop that appends the information retrieved from 'samplefile_t8.txt' into 'fileList'
    for list in x:
        list = list.strip(',"\n')
        fileList.append(list)
        count = count + 1
    #while-loop that appends the list entries from 'fileList' into 'fileDisplay' using the specifications of 'fileIt'
    while it <= count:
        #error check in case the range of 'it' starts below or equal to zero
        if it <= 0:
            print("Error, range must be greater than 0 for file readout.")
            break
        fileDisplay.append(fileList[it-1])
        it = it + fileIt
    #error check in case of 'fileDisplay' printing nothing
    if (fileDisplay == []):
        print ("An error has occured, please enter a valid range for file readout.")
    #prints the appended 'fileDisplay' list with the iterations from 'fileIt'
    else:
        print(fileDisplay)
    #closes 'sampleFile_t8.txt'
    f.close()

def main():
    filereader("samplefile_t8.txt", 3)

if __name__ == "__main__":
    main()
