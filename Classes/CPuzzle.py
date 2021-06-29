﻿from .CState import CState
import nPuzzle.UtilsSearch.search as search


from pynput import keyboard


class CPuzzle :
    def __init__(self,size,startNode):
        self.startNode = startNode
        self.size = size
        self.goal = self.getGoal(size)
        self.open = []
        self.close = []
        self.listen = True
        self.maxOpen = 0
        self.nbOpenSelected = 0

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

    def execution(self, opt) :
        elem = None
        for a, o in opt : 
            if (a == '-a' and o == 'ida'):
               elem = search.idaStar(self)
            if (a == '-a' and o == 'aStar'):
               elem = search.aStar(self)
        if (not elem) : 
            elem = search.aStar(self)
        if (elem) :
            while elem.daddy != None:
                print(elem)
                elem = elem.daddy
        print(self.startNode)