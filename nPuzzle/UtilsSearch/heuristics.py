def hManhattan(self, table, goal):
    ret = 0
    for i in range(self.state.size * self.state.size):
        if table[i] != 0 and table[i] != goal[i]:
            casei = goal.index(table[i])
            y = (i // self.state.size) - (casei // self.state.size)
            x = (i % self.state.size) - (casei % self.state.size)
            ret += abs(y) + abs(x)
    return ret

