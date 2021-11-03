def hchosen(node, table, goal, htab) :
    ret = 0
    for hFunc in htab :
        ret += hFunc(node, table, goal)
    return ret

def hDumb(node, table, goal):
    ret = 0
    size = node.state.size
    for i in range(node.state.size * node.state.size):
        if table[i] != goal[i]:
            ret += 1 
    node.hDumb = ret
    return ret

def hManhattan(node, table, goal):
    ret = 0
    size = node.state.size
    for i in range(node.state.size * node.state.size):
        if table[i] != 0 and table[i] != goal[i]:
            casei = goal.index(table[i])
            y = (i // size) - (casei // size)
            x = (i % size) - (casei % size)
            ret += abs(y) + abs(x)
    node.hManhattan = ret
    return ret

def hManhattanOneTile(node, table, goal):
    
    ret = node.daddy.hManhattan
    size = node.state.size
    
    x, y = node.daddy.state.voidPos
    tile = table[y * size + x]
    x2, y2 = getCoord1DTo2D(goal.index(tile) , size)
    ret += abs(x - x2) + abs(y - y2)
    
    x, y = node.state.voidPos
    ret -= abs(x - x2) + abs(y - y2)
    
    node.hManhattan = ret
    return ret

def getCoord1DTo2D(index , size) :
    x = index % size
    y = index // size

    return x,y


def hLinearConflict(node, table, goal) :
    ret = 0
    length = node.state.size * node.state.size
    size = node.state.size
    for iTuile in range(1, length) :
        for jTuile in range(iTuile + 1, length) :

            xiGoal, yiGoal = getCoord1DTo2D(goal.index(iTuile), size)
            xjGoal, yjGoal = getCoord1DTo2D(goal.index(jTuile), size)
            # on test si les deux tuile sont sur la même ligne 
            if yiGoal == yjGoal:
                xi, yi = getCoord1DTo2D(table.index(iTuile), size)
                xj, yj = getCoord1DTo2D(table.index(jTuile), size)
                if yi == yj and yi == yiGoal :
                    if  not ((xiGoal - xjGoal < 0 and xi - xj < 0 ) or (xiGoal - xjGoal > 0 and xi - xj > 0)) :
                        ret += 2
            elif xiGoal == xjGoal :
                xi, yi = getCoord1DTo2D(table.index(iTuile), size)
                xj, yj = getCoord1DTo2D(table.index(jTuile), size)
                if xi == xj and xi == xiGoal:
                    if  not ((yiGoal - yjGoal < 0 and yi - yj < 0 ) or (yiGoal - yjGoal > 0 and yi - yj > 0)) :
                        ret += 2
    node.hLinear = ret
    
    return ret
def hLinearConflictThatTile(node, table, goal, iTuile) :
    ret = 0
    size = node.state.size
    length = node.state.size * node.state.size
    
    for jTuile in range(1, length) :
        if iTuile != jTuile :
            xiGoal, yiGoal = getCoord1DTo2D(goal.index(iTuile), size)
            xjGoal, yjGoal = getCoord1DTo2D(goal.index(jTuile), size)
            # on test si les deux tuile sont sur la même ligne 
            if yiGoal == yjGoal:
                xi, yi = getCoord1DTo2D(table.index(iTuile), size)
                xj, yj = getCoord1DTo2D(table.index(jTuile), size)
                if yi == yj and yi == yiGoal :
                    if  not ((xiGoal - xjGoal < 0 and xi - xj < 0 ) or (xiGoal - xjGoal > 0 and xi - xj > 0)) :
                        ret += 2
            elif xiGoal == xjGoal :
                xi, yi = getCoord1DTo2D(table.index(iTuile), size)
                xj, yj = getCoord1DTo2D(table.index(jTuile), size)
                if xi == xj and xi == xiGoal:
                    if  not ((yiGoal - yjGoal < 0 and yi - yj < 0 ) or (yiGoal - yjGoal > 0 and yi - yj > 0)) :
                        ret += 2
    return ret

def hLinearConflictOneTile(node, table, goal) :
    ret = node.daddy.hLinear
    size = node.state.size
    x, y = node.daddy.state.voidPos
    iTuile = table[y * size + x]
    
    ret -= hLinearConflictThatTile(node.daddy, node.daddy.state.table, goal, iTuile)

    ret += hLinearConflictThatTile(node, table, goal, iTuile)
    
    node.hLinear = ret
    return ret

def hCornerConflictEight(node, table, goal) :
    ret = 0
    size = node.state.size
    upLeft = False
    upRigth = False
    downLeft = False
    # upLeft
    if table[0] != 0 and table[0] != goal[0] :
        if table[1] == goal[1] and table[size] == goal[size] :
            ret += 4
            upLeft = True
    # upRigth
    if not upLeft and table[size - 1] != 0 and table[size - 1] != goal[size - 1] :
        if table[size - 2] == goal[size - 2] and table[2 * size - 1] == goal[2 * size - 1] :
            ret += 4
            upRigth = True
    # downLeft
    if not upLeft and table[size * size - size] != 0 and table[size * size - size] != goal[size * size - size] :
        if table[size * size - size * 2] == goal[size * size - size * 2] and table[size * size - size + 1] == goal[size * size - size + 1] :
            ret += 4
            downLeft = True
    # downRigth
    if not downLeft and not upRigth and table[size * size - 1] != 0 and table[size * size - 1] != goal[size * size - 1] :
        if table[size * size - 2] == goal[size * size - 2] and table[size * size - size - 1] == goal[size * size - size - 1] :
            ret += 4
    return ret

def hCornerConflict(node, table, goal) :
    ret = 0
    size = node.state.size
    # upLeft
    if table[0] != 0 and table[0] != goal[0] :
        if table[1] == goal[1] and table[size] == goal[size] :
            ret += 4
    # upRigth
    if table[size - 1] != 0 and table[size - 1] != goal[size - 1] :
        if table[size - 2] == goal[size - 2] and table[2 * size - 1] == goal[2 * size - 1] :
            ret += 4
    # downLeft
    if table[size * size - size] != 0 and table[size * size - size] != goal[size * size - size] :
        if table[size * size - size * 2] == goal[size * size - size * 2] and table[size * size - size + 1] == goal[size * size - size + 1] :
            ret += 4
    # downRigth
    if table[size * size - 1] != 0 and table[size * size - 1] != goal[size * size - 1] :
        if table[size * size - 2] == goal[size * size - 2] and table[size * size - size - 1] == goal[size * size - size - 1] :
            ret += 4
    return ret