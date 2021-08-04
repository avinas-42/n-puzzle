from nPuzzle.UtilsSearch.heuristics import hchosen
from .CState import CState
class CNode :
    def __init__(self, state, level, fScore):
        self.state = state
        self.level = level
        self.fScore = fScore
        self.hManhattan = 0
        self.hLinear = 0
        self.daddy = None
        
        

    def getChildren(self, goal):
        x, y = self.state.voidPos
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            if(i[0] >= 0 and i[0] < self.state.size and i[1] >= 0 and i[1] < self.state.size):
                
                tmpState = CState(self.state.size, self.state.table.copy())
                tmpState.swap(x, y, i[0], i[1])
                # on verifie que le daddy du daddy (node.daddy) nest pas le child
                if  self.daddy and tmpState.table == self.daddy.state.table :
                    del tmpState
                    continue
                tmpState.voidPos = tmpState.getVoidPos()
                tmpNode = CNode(tmpState, self.level + 1, 0)
                # tmpNode.fScore = tmpNode.f(goal)
                tmpNode.daddy = self
                children.append(tmpNode)
        return children

    def f(self, goal, hTab):
        return hchosen(self, self.state.table, goal, hTab) + self.level
    def fSpeed(self, goal, hSpeedTab) :
        return hchosen(self, self.state.table, goal, hSpeedTab) + self.level
    def h(self, goal, hTab):
        return hchosen(self, self.state.table, goal, hTab)
    def hSpeed(self, goal, hSpeedTab) :
        return hchosen(self, self.state.table, goal, hSpeedTab)
    def __lt__(self, other) :
        return self.fScore < other.fScore
    def __repr__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret
    def __str__(self):
        ret = "level = " + str(self.level) +" | " + " fScore = " + str(self.fScore) + " state =\n" + str(self.state)
        return ret