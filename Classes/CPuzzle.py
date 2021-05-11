from pynput import keyboard

class CPuzzle :
    def __init__(self,size,startNode):
        self.startNode = startNode
        self.size = size
        self.goal = list(range(1,size*size))
        self.goal.append(0)
        self.open = []
        self.closed = []
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

    def hscore(self, case, goal):
        ret = 0
        for i in range(self.size * self.size):
            if case[i] != 0 and case[i] != goal[i]:
                casei = goal.index(case[i])
                y = (i // self.size) - (casei // self.size)
                x = (i % self.size) - (casei % self.size)
                ret += abs(y) + abs(x)
        return ret

