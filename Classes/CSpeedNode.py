import numpy as np
class CSpeedNode :
    def __init__(self, node, table, fScore, level):
        self.node = node
        self.table = np.array(table, dtype=np.uint16).tobytes()
        # self.table = table
        self.fScore = fScore
        self.level = level

    def __eq__(self,  other) :
        # return np.array_equal(self.table , other.table) and self.fScore > other.fScore
        return self.table == other.table and self.fScore > other.fScore
    def __lt__(self, other) :
        return self.fScore <= other.fScore