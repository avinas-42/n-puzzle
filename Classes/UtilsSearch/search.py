import sys
import bisect
from collections import deque
def aStar(puzzle) :
        puzzle.startNode.fScore = puzzle.startNode.f(puzzle.goal.table)
        if puzzle.startNode.fScore == 0 :
            print(puzzle.startNode)
            return
        
        puzzle.open.append(puzzle.startNode)
        cpt = 0
        while not(len(puzzle.open) == 0):
            if puzzle.open[0].fScore - puzzle.open[0].level ==  0 :
                return puzzle.open[0]
            if cpt % 1000 == 0 or cpt == 0:
                print(puzzle.open[0].fScore)

            cpt += 1

            tabChild = puzzle.open[0].getChildren(puzzle.goal.table)
            for child in tabChild:
                if any(child.state.table == elem.state.table for elem in puzzle.close):
                    continue
                if any(child.state.table == elem.state.table and child.fScore > elem.fScore for elem in puzzle.open):
                    continue
                else : 
                    bisect.insort_left(puzzle.open, child)
            puzzle.close.append(puzzle.open.pop(0))
        return None

def idaSearch(node, threshold, puzzle) :
    node.fScore = node.f(puzzle.goal.table)
    if node.fScore > threshold :
        return node.fScore, None
    if node.fScore - node.level == 0 :
        return node.fScore, node
    fmin = sys.maxsize

    for child in node.getChildren(puzzle.goal.table) :
        if  node.daddy != None and child.state.table == node.daddy.state.table :
            continue
        temp, found = idaSearch(child, threshold, puzzle)
        if found != None :
            return temp, found
        if temp < fmin :
            fmin = temp
    return fmin, None

def idaStar(puzzle) :
    puzzle.startNode.fScore = puzzle.startNode.f(puzzle.goal.table)
    found = None
    threshold = puzzle.startNode.fScore

    while found == None :
        temp, found = idaSearch(puzzle.startNode, threshold, puzzle)
        threshold = temp
        print(threshold)
    return found
