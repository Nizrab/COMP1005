def find_diff(mylst):
    oneD = []
    rows = len(mylst)
    for i in range(0,rows):
        list1 = max(mylst[i])-min(mylst[i])
        oneD.append(list1)
    return oneD

mylst = [[2,3,6],
         [5,4,1],
         [3,7,9,8]]
res = find_diff(mylst)
print(res)
