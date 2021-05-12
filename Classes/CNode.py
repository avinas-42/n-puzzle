from .CState import CState
class CNode :
    def __init__(self, state, level, fScore):
        self.state = state
        self.level = level
        self.fScore = fScore
        self.daddy = None

    def getChildren(self):
        x, y = self.state.voidPos
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            if(i[0] >= 0 and i[0] < self.state.size and i[1] >= 0 and i[1] < self.state.size):
                
                tmpState = CState(self.state.size, self.state.table.copy())
                tmpState.swap(x, y, i[0], i[1])
                tmpNode = CNode(tmpState, self.level + 1, 0)
                tmpNode.daddy = self
                children.append(tmpNode)
        return children

    def hscore(self, case, goal):
        ret = 0
        for i in range(self.size * self.size):
            if case[i] != 0 and case[i] != goal[i]:
                casei = goal.index(case[i])
                y = (i // self.size) - (casei // self.size)
                x = (i % self.size) - (casei % self.size)
                ret += abs(y) + abs(x)
        return ret

    def fscore(self, case, goal):
        return self.hscore(case.state, goal) + case.level

    def __repr__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret
    def __str__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret