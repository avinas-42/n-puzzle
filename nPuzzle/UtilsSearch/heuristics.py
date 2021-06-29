def hLinehaTtan(node, table, goal) :
    ret = hManhattan(node, table, goal )
    ret += hLinearConflict(node, table, goal )
    return ret

def hManhattan(node, table, goal):
    ret = 0
    for i in range(node.state.size * node.state.size):
        if table[i] != 0 and table[i] != goal[i]:
            casei = goal.index(table[i])
            y = (i // node.state.size) - (casei // node.state.size)
            x = (i % node.state.size) - (casei % node.state.size)
            ret += abs(y) + abs(x)
    return ret

def getCoord1DTo2D(index , size) :
    x = index % size
    y = index // size

    return x,y


def hLinearConflict(node, table, goal) :
    ret = 0
    size = node.state.size * node.state.size
    for iTuile in range(1, size) :
        for jTuile in range(iTuile + 1, size) :

            xiGoal, yiGoal = getCoord1DTo2D(goal.index(iTuile), node.state.size)
            xjGoal, yjGoal = getCoord1DTo2D(goal.index(jTuile), node.state.size)
            # on test si les deux tuile sont sur la même ligne 
            if yiGoal == yjGoal:
                xi, yi = getCoord1DTo2D(table.index(iTuile), node.state.size)
                xj, yj = getCoord1DTo2D(table.index(jTuile), node.state.size)
                if yi == yj and yi == yiGoal :
                    if  not ((xiGoal - xjGoal < 0 and xi - xj < 0 ) or (xiGoal - xjGoal > 0 and xi - xj > 0)) :
                        # print (str(iTuile) + ' - ' + str(jTuile))
                        # print ('xi : ' + str(xiGoal) +' | yi : ' + str(yiGoal) +' \n xj : ' + str(xjGoal) +' | yj : ' + str(yjGoal))
                        # print (str(iTuile) + ' - ' + str(jTuile))
                        # print ('xi : ' + str(xi) +' | yi : ' + str(yi) +' \n xj : ' + str(xj) +' | yj : ' + str(yj))
                        ret += abs(xi - xj) * 2
            elif xiGoal == xjGoal :
                xi, yi = getCoord1DTo2D(table.index(iTuile), node.state.size)
                xj, yj = getCoord1DTo2D(table.index(jTuile), node.state.size)
                if xi == xj and xi == xiGoal:
                    if  not ((yiGoal - yjGoal < 0 and yi - yj < 0 ) or (yiGoal - yjGoal > 0 and yi - yj > 0)) :
                        ret += abs(yi - yj) * 2
    return ret
            
