from nPuzzle.UtilsSearch.searchEnum import Search
from nPuzzle.UtilsSearch.heuristics import hManhattan

from Classes.CPuzzle import CPuzzle
import sys
import bisect

def searching(puzzle, search) :
    if (search == Search.IDA):
        return idaStar(puzzle)
    if (search != Search.UNIFORM):    
        puzzle.startNode.fScore = puzzle.startNode.f(puzzle.goal.table, CPuzzle.hTab)
    open = []
    seen = []
    goal = puzzle.goal.table
    open.append(puzzle.startNode)
    seen.append(puzzle.startNode.state.table)
    
    while not(len(open) == 0):
        if (search == Search.ASTAR):
            if open[0].fScore - open[0].level ==  0 :
                return open[0]
        elif (search == Search.GREEDY):
            if open[0].fScore ==  0 :
                return open[0]
        elif (search == Search.UNIFORM):

            if open[0].h(goal, [hManhattan]) == 0:
                return open[0]

        puzzle.nbOpenSelected += 1 
        tabChild = open[0].getChildren(goal)
        open.pop(0).state.table
        for child in tabChild:
            if child.state.table in seen :
                continue
            if (search == Search.ASTAR):
                child.fScore = child.fSpeed(goal, CPuzzle.hSpeedTab)
            elif (search == Search.GREEDY):
                child.fScore = child.hSpeed(goal, CPuzzle.hSpeedTab)
            elif (search == Search.UNIFORM):
                child.fScore = child.level
            
            bisect.insort_left(open, child)
            seen.append(child.state.table)
            if puzzle.maxOpen < len(open):
                puzzle.maxOpen = len(open)

    return None
    
def idaSearch(node, threshold, puzzle) :
    if node.daddy != None : 
        node.fScore = node.fSpeed(puzzle.goal.table, CPuzzle.hSpeedTab)
    else :
        node.fScore = node.f(puzzle.goal.table, CPuzzle.hTab)
    if node.fScore > threshold :
        return node.fScore, None
    if node.fScore - node.level == 0 :
        return node.fScore, node
    fmin = sys.maxsize

    puzzle.nbOpenSelected += 1
    for child in node.getChildren(puzzle.goal.table) :
        puzzle.maxOpen += 1
        # recurssif idaSearch sur les enfant du noeud
        temp, found = idaSearch(child, threshold, puzzle)
        if found != None :
            return temp, found
        # on garde le fScore minimum (fScore = g + h)
        if temp < fmin :
            fmin = temp
    return fmin, None

def idaStar(puzzle) :
    puzzle.startNode.fScore = puzzle.startNode.f(puzzle.goal.table, CPuzzle.hTab)
    found = None
    threshold = puzzle.startNode.fScore
    while found == None :
        threshold, found = idaSearch(puzzle.startNode, threshold, puzzle)
        # on revien ici quand la tolerence sur le fScore augmente
    return found