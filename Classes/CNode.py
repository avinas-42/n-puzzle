from .CState import CState
class CNode :
    def __init__(self, state, level, fScore, hFunc):
        self.state = state
        self.level = level
        self.fScore = fScore
        self.daddy = None
        self.children = []
        CNode.hFunc = hFunc 

    def getChildren(self, goal):
        x, y = self.state.voidPos
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            if(i[0] >= 0 and i[0] < self.state.size and i[1] >= 0 and i[1] < self.state.size):
                
                tmpState = CState(self.state.size, self.state.table.copy())
                tmpState.swap(x, y, i[0], i[1])
                tmpState.voidPos = tmpState.getVoidPos()
                tmpNode = CNode(tmpState, self.level + 1, 0, CNode.hFunc)
                tmpNode.fScore = tmpNode.f(goal)
                tmpNode.daddy = self
                children.append(tmpNode)
        return children



    def f(self, goal):
        return CNode.hFunc(self,self.state.table, goal) + self.level

    def __lt__(self, other):
        return self.fScore <= other.fScore
    def __repr__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret
    def __str__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret