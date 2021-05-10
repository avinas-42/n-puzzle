﻿from .CState import CState
class CNode :
    def __init__(self, state, level, fScore):
        self.state = state
        self.level = level
        self.fScore = fScore

    def getChildren(self):
        x, y = self.state.voidPos
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            if(i[0] >= 0 and i[0] < self.state.size and i[1] >= 0 and i[1] < self.state.size):
                
                tmpState = CState(self.state.size, self.state.table.copy())
                tmpState.swap(x, y, i[0], i[1])
                tmpNode = CNode(tmpState, self.level + 1, 0)
                children.append(tmpNode)
        return children
    
    def __repr__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret
    def __str__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret