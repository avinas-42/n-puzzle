from nPuzzle.UtilsSearch.heuristics import hchosen
from .CState import CState
class CNode :
    def __init__(self, state, level, fScore, hTab):
        self.state = state
        self.level = level
        self.fScore = fScore
        self.daddy = None
        self.children = []
        CNode.hTab = hTab 

    def getChildren(self, goal):
        x, y = self.state.voidPos
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            if(i[0] >= 0 and i[0] < self.state.size and i[1] >= 0 and i[1] < self.state.size):
                
                tmpState = CState(self.state.size, self.state.table.copy())
                tmpState.swap(x, y, i[0], i[1])
                # on verifie que le daddy du daddy (node.daddy) nest pas le child
                if  self.daddy != None and tmpState.table == self.daddy.state.table :
                    del tmpState
                    continue
                tmpState.voidPos = tmpState.getVoidPos()
                tmpNode = CNode(tmpState, self.level + 1, 0, CNode.hTab)
                # tmpNode.fScore = tmpNode.f(goal)
                tmpNode.daddy = self
                children.append(tmpNode)
        return children

    def f(self, goal):
        return hchosen(self, self.state.table, goal, CNode.hTab) + self.level

    def __lt__(self, other):
        return self.fScore <= other.fScore
    def __repr__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret
    def __str__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret