VOID = 0
class CState :
    def __init__(self, size, table):
        self.size = size
        self.table = table
        self.voidPos = self.getVoidPos()

    def swap(self, x1, y1, x2, y2):
        self.table[x1 + y1 * self.size] = self.table[x1 + y1 * self.size] + self.table[x2 + y2 * self.size]
        self.table[x2 + y2 * self.size] = self.table[x1 + y1 * self.size] - self.table[x2 + y2 * self.size] 
        self.table[x1 + y1 * self.size] = self.table[x1 + y1 * self.size] - self.table[x2 + y2 * self.size]

    def getVoidPos(self):
        index = self.table.index(VOID) 
        y = index // self.size
        x = index % self.size 
        return x, y

    def getTile(self, x, y):
        return self.table[x + y * self.size]

    def setTile(self, x, y, value):
        self.table[x + y * self.size] = value

    def __str__(self):
        ret = "size = " + str(self.size) +"\n|"
        for i in range(len(self.table)):
            ret += "\t" + str(self.table[i]) + "\t|"
            if ((i + 1) % self.size == 0 and i + 1 < len(self.table) ) :
                ret += "\n|"
        ret += "\n"
        return ret
