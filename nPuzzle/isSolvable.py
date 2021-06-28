def inversion(table, size) :
    inversion = 0

    for i in range(0, size - 1) :
        for j in range(i + 1, size - 1) :
            # print(str(i)+' | '+str(j))
            if table.index(i) > table.index(j) :
                inversion += 1
    return inversion

def isSolvable(start, goal) :
    
    startInversion = inversion(start.table, start.size * start.size)
    goalInversion = inversion(goal.table, goal.size * goal.size)

    if startInversion % 2 == goalInversion % 2 :
        return True
    return False
