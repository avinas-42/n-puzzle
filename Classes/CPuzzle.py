from pynput import keyboard
def getKey(obj):
    return obj.fScore
class CPuzzle :
    def __init__(self,size,startNode):
        self.startNode = startNode
        self.size = size
        self.goal = list(range(1,size*size))
        self.goal.append(0)
        self.open = []
        self.close = []
        self.listen = True

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
        tabChild = self.startNode.getChildren(self.goal)
        tabChild.sort(key=getKey)
        self.open += tabChild
        self.close.append(self.startNode)
        cpt = 0
        while 1:
            cpt += 1 
            # if cpt % 500 == 0:
            #     print(self.open[0])
            if self.open[0].fScore - self.open[0].level == 0 or len(self.open) == 0:
                break
            tabChild = self.open[0].getChildren(self.goal)
            for elem in self.close:    
                for child in tabChild:
                    if child.state.table == elem.state.table:
                            tabChild.remove(child)
            self.open += tabChild
            self.close.append(self.open[0])
            self.open.pop(0)
            self.open.sort(key=getKey)
            print(self.open)
            print("----------------------------------")
        elem = self.open[0]
        while elem.daddy != None:
            print(elem)
            elem = elem.daddy
