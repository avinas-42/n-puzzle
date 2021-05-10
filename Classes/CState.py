class CState :
    def __init__(self, size, table):
        self.size = size
        self.table = table
    
    def swap(self, x1, y1, x2, y2):
        self.table[x1 + y1 * self.size] = self.table[x1 + y1 * self.size] + self.table[x2 + y2 * self.size]
        self.table[x2 + y2 * self.size] = self.table[x1 + y1 * self.size] - self.table[x2 + y2 * self.size] 
        self.table[x1 + y1 * self.size] = self.table[x1 + y1 * self.size] - self.table[x2 + y2 * self.size]
    
    def getTile(self, x, y):
        return self.table[x + y * self.size]

    def setTile(self, x, y, value):
        self.table[x + y * self.size] = value


    def __str__(self):
        ret = str(self.size) +"\n|"
        for i in range(len(self.table)):
            ret += "\t" + str(self.table[i]) + "\t|"
            if ((i + 1) % self.size == 0 and i + 1 < len(self.table) ) :
                ret += "\n|"
        return ret
        
