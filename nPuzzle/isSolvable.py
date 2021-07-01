def inversion(table, size) :
    inversion = 0
    for i in range(1, size) :
        for j in range(i + 1, size) :
            if table.index(i) > table.index(j) :
                # print(str(i)+' | '+ str(j))
                inversion += 1
    return inversion

def isSolvable(start, goal) :
    
    startInversion = inversion(start.table, start.size * start.size)
    # print('---------------------')
    goalInversion = inversion(goal.table, goal.size * goal.size)
    # print(startInversion)
    # print(goalInversion)
    if startInversion % 2 == goalInversion % 2 :
        return True
    return False
