from pynput import keyboard
from .CState import CState
import bisect

def getKey(obj):
    return obj.fScore
class CPuzzle :
    def __init__(self,size,startNode):
        self.startNode = startNode
        self.size = size
        self.goal = self.getGoal(size)
        self.open = []
        self.close = []
        self.listen = True

    def nextdirection(self, direction) :
        if direction + 1 > 3 :
            direction = 0
        else :
            direction += 1
        return direction

    def forward(self, direction, pos) :
        nextPos = [0,0]
        nextPos[0] = pos[0]
        nextPos[1] = pos[1]
        if direction == 0 :
            nextPos[0] = pos[0] + 1 
        elif direction == 1 :
            nextPos[1] = pos[1] + 1
        elif direction == 2 :
            nextPos[1] = pos[1] - 1 
        elif direction == 3 :
            nextPos[0] = pos[0] - 1
        return nextPos

    def getGoal(self, size) :
        table = [0] * (self.size * self.size)
        state = CState(size, table = table)
        pos = [0, 0]
        direction = 0
        nextPos = [0,0]
        value = 1

        while state.table.count(0) > 1 :            
            if nextPos[0] >= 0 and nextPos[0] < self.size and nextPos[1] >= 0 and nextPos[1] < self.size :
                if state.getTile(nextPos[0], nextPos[1]) == 0 :
                    pos[0] = nextPos[0]
                    pos[1] = nextPos[1]
                    state.setTile(pos[0], pos[1], value)
                    value += 1
                else :
                    direction = self.nextdirection(direction)
            else :
                direction = self.nextdirection(direction)
            nextPos = self.forward(direction ,pos)
        return state

    def play(self) :
        print(self.startNode.state)
        self.initKeyboard()
    
    def on_release(self, key):

        if key == keyboard.Key.esc:
            self.listen = False 
            return False
        elif key == keyboard.Key.up:
            action = [0,-1]
        elif key == keyboard.Key.down:
            action = [0,1]
        elif key == keyboard.Key.left:
            action = [-1,0]
        elif key == keyboard.Key.right:
            action = [1,0]
        else:
            return True

        state = self.startNode.state
        if(state.voidPos[0] + action[0] >= 0 and state.voidPos[0] + action[0] < state.size 
        and state.voidPos[1] + action[1] >= 0 and state.voidPos[1] + action[1] < state.size):
            state.swap(state.voidPos[0], state.voidPos[1], state.voidPos[0] + action[0], state.voidPos[1] + action[1])
            state.voidPos = state.getVoidPos()
        print(state)

    def initKeyboard(self) :
        listener = keyboard.Listener(
            on_release=self.on_release)
        listener.start()
        while(self.listen):
            pass
    
    def execution(self) :
        # print(self.goal)
        self.startNode.fScore = self.startNode.f(self.goal.table)
        if self.startNode.fScore == 0 :
            print(self.startNode)
            return
        
        self.open.append(self.startNode)
        cpt = 0
        while not(len(self.open) == 0 or self.open[0].fScore - self.open[0].level == 0):
            if cpt % 1000 == 0 or cpt == 0:
                print(self.open[0].fScore)
                

            cpt += 1
            
            tabChild = self.open[0].getChildren(self.goal.table)
            for child in tabChild:
                if any(child.state.table == elem.state.table for elem in self.close):
                    continue
                if any(child.state.table == elem.state.table and child.fScore > elem.fScore for elem in self.open):
                    continue
                else : 
                    bisect.insort_left(self.open, child)
                    

            self.close.append(self.open.pop(0))
            
            # self.open.sort(key=getKey)

        print("--------------------------")

        elem = self.open[0]
        while elem.daddy != None:
            print(elem)
            elem = elem.daddy
        print(self.startNode)