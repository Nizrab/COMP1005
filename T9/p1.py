def display(dicts):
    if not dicts:
        print('No Data In List')
    else:
        for i in sorted(dicts.items()) :
            print(str(i[0])+":", i[1] )



d = {'a':1, 'b':2, 'c':3}
print(d)
display(d)
