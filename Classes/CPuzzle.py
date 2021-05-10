class CPuzzle :
    def __init__(self,size):
        self.size = size
        self.goal = list(range(1,size*size))
        self.goal.append(0)
        self.open = []
        self.closed = []

