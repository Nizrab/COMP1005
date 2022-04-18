# Test 2 - Problem 4
def words_with_xchar(list, c, x):
    new = []
    dim0 = 0
    dim1 = 0
    while (dim0 < len(list)):
        while (dim1 < len(list[dim0])):
            if ((len(list[dim0][dim1]) <= x) & (list[dim0][dim1][0] == c)):
                new.append(list[dim0][dim1])
            dim1 = dim1 + 1
        dim1 = 0
        dim0 = dim0 + 1
    return new
list = [['789', 'del'], ['a', 'd'], ['bb', 'do'], ['dcc'], ['dddd', 'duck'], ['efghi', 'd#$%^'], ['zzzzzzzzz']]
print(words_with_xchar(list, "d", 4))