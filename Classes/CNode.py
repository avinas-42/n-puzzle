from .CState import CState
class CNode :
    def __init__(self, state, level, fScore):
        self.state = state
        self.level = level
        self.fScore = fScore
        self.daddy = None

    def getChildren(self, goal):
        x, y = self.state.voidPos
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            if(i[0] >= 0 and i[0] < self.state.size and i[1] >= 0 and i[1] < self.state.size):
                
                tmpState = CState(self.state.size, self.state.table.copy())
                tmpState.swap(x, y, i[0], i[1])
                tmpState.voidPos = tmpState.getVoidPos()
                tmpNode = CNode(tmpState, self.level + 1, 0)
                tmpNode.fScore = tmpNode.f(goal)
                tmpNode.daddy = self
                children.append(tmpNode)
        return children

    def h(self, table, goal):
        ret = 0
        for i in range(self.state.size * self.state.size):
            if table[i] != 0 and table[i] != goal[i]:
                casei = goal.index(table[i])
                y = (i // self.state.size) - (casei // self.state.size)
                x = (i % self.state.size) - (casei % self.state.size)
                ret += abs(y) + abs(x)
        return ret

    def f(self, goal):
        return self.h(self.state.table, goal) + self.level

    def __lt__(self, other):
        return self.fScore <= other.fScore
    def __repr__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret
    def __str__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret