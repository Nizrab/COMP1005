"""
Name: Barzin Farahani
Student ID: 101256924
Date: 2022/03/27

"""

#display_list Method
def display_list(arr):
    #Checks if data is in the array
    if not arr:
        print('No Data In List')
    #Prints the array
    else:
        for i in arr:
            print(i)
#display_dict Method
def display_dict(dicts):
    #Checks if data is in the dictionary
    if not dicts:
        print('No Data In List')
    #Prints the dictionary
    else:
        for i in sorted(dicts.items()) :
            print(str(i[0])+":", i[1] )
#load_data Method
def load_data(file):
    #Opens the file
    with open(file, "r") as f:
        #Skips the header
        next(f)
        #Meber variabes
        record = []
        displayArr = []
        #Loops through file
        for i in f:
            data = i.strip().split(",")
            record.append(data)
        #inclues specifided colloums
        cols = [1,3,4,5,6,7,8,9]
        #Loops through record array with appended data
        for row in record:
            #Will go through spesificed colloums
            content = list(row[i] for i in cols)
            #Then appends the content of these colloums to displayArr
            displayArr.append(content)
        #Returns the array
        return displayArr
#region_dict Method
def region_dict(file):
    #Opens the file
    with open(file, "r") as f:
        #Skips the Header
        next(f)
        #Member variables
        regions = {}
        values = []
        buff = {}
        #loops through the whole file
        for i in f:
            data = i.strip().split(",")
            #appends the data to values
            values.append(data[1])
            #Sets the names to values
            regions[data[0]] = values
            #Checks if the data is a key
            if data[0] not in buff.keys():
                #If so will update what is already there appending the new value
                buff.update({data[0]:data[1]})
            else:
                #Else will loop through the keys
                for x in buff.keys():
                    #Check if the value is equal to a key
                    if data[0] == x:
                        #Checks for the instance
                        if isinstance(buff[x], list):
                            temp2 = buff[data[0]]
                            #append the data to a list
                            temp2.append(data[1])
                            #Then updates the buffer
                            buff.update({data[0]:temp2})
                        elif isinstance(x, str):
                            temp = [x]
                            #else will appened the new item x to temp
                            temp.append(data[1])
                            #Then will create a new key with said item
                            buff.update({x:temp})
        for a in buff.keys():
            temp = buff[a]
            if isinstance(temp, list):
                temp.pop(0)
                buff.update({a:temp})
        #Retuns the buffer dictionary
        return buff
#prov_dict Method
def prov_dict(file):
    #Opens the file
    with open(file, "r") as f:
        #Skips the header
        next(f)
        #dictionary
        provinces = {}
        sprovinces = {}
        values = []
        #Gose through entire file
        for i in f:
            data = i.strip().split(",")
            #appends the value to array
            values.append(data[1])
            #Sorts the array
            values.sort()
            provinces[data[1]] = data[2]
        #Returns the dictionary
        return provinces
#prov_records_per_date Method
def prov_records_per_date(database,pId):
    #Member variables
    allICU = 0
    id = []
    date = []
    #Gose through database to add up all of the people in ICU
    for i in database:
        allICU = int(i[2])+ int(i[3])+int(i[4])+int(i[5])+int(i[6])+int(i[7])
        if pId == int(i[0]):
            #Will add the specifided date of that PID aswell as all in the ICU
            date.append([i[1],allICU])
    return date

#prov_total_cases Method
def prov_total_cases(database,pId):
    #Member variables
    allICU = 0
    x = 0
    date = []
    #Gose through database to add up all of the people in ICU
    for i in database:
        allICU = int(i[2])+ int(i[3])+int(i[4])+int(i[5])+int(i[6])+int(i[7])
        #If PID is equal then adds all of the values above together
        if pId == int(i[0]):
             x = x + allICU
             date.append([allICU])
    return x
#prov_vac_status Method
def prov_vac_status(database,pId):
    x = 0
    y = 0
    z = 0
    #Goes through the database
    for i in database:
        #Setting all the vax and unvax data
        unVAc = int(i[2])
        icu_part_vac = int(i[3])
        icu_full_vac = int(i[4])
        #If PID is equal then adds to the x values
        if pId == int(i[0]):
            x = x + unVAc
            y = y + icu_part_vac
            z = z + icu_full_vac
    return x,y,z

#-------------------------------------------------------------------

def main():
    #while statment to loop input incase of error
    while True:
        #Takes user input for file name
        filename = input("Please enter the name of the file you want to use: ")
        #Checks if it is able to open the file
        try:
            with open(filename) as f:
                print("File Obtained")
                break
        #FileNotFoundError check
        except FileNotFoundError:
            print('File does not exist')
            continue

    database = load_data(filename)
    print("Data loaded.")

    print("\nDisplaying data")
    display_list(database)
    regions = region_dict(filename)
    print("\nDisplaying the regions dictionary")
    display_dict(regions)
    provinces = prov_dict(filename)
    print("\nDisplaying the provices dictionary")
    display_dict(provinces)

    print("\nPrinting province-wise data analysis")
    id = 0
    #while statment to loop input incase of error
    while True:
        try:
            id = int(input("Please enter A province ID: "))
            break
        #catches ValueError
        except ValueError:
            print("Input Error")
            continue

    print("\nPrinting the prov_records_per_date()")
    results = prov_records_per_date(database, id)
    display_list(results)

    print("\nPrinting the prov_total_cases()")
    tot_cases = prov_total_cases(database, id)
    print(tot_cases)

    print("\nPrinting the prov_vac_status()")
    res1, res2, res3 = prov_vac_status(database, id)
    print(f"{res1}, {res2}, {res3}")

if __name__ == "__main__":
    main()
