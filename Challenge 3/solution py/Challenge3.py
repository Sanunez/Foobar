x = 3
y = 2

def answer(x, y):
    trindex = x + y
    print trindex
    tri = ((trindex-1) * trindex) / 2
    final = tri - (y-1)
    return str(final)

    '''
    def returnValue(list, x, y):
        return str(list[x+y][y])
    def remove_values_from_list(the_list, val):
        return [value for value in the_list if value != val]
    length = ((y-1) + x)
    cellnum = ((length*(length+1))/2)
    cells = range(1, cellnum+1)
    count = range(1, cellnum+1)
    x -= 1
    y -= 1
    #Create Grid with zeros
    prison = [[0 for i in range(0,length)] for j in range(0,length)]
    #Populate Grid
    for i in range(0, length):
        for j in range(0,count.pop(0)):
            prison[i].insert(0,cells.pop(0))
            prison[i] = remove_values_from_list(prison[i], 0)
    #fill zeroes
    for i in range(0,length):
        while len(prison[i]) != length:
            prison[i].append(0)
    '''
answer(x,y)
