from Classes.CPuzzle import CPuzzle
import sys
import bisect

def aStar(puzzle) :
        puzzle.startNode.fScore = puzzle.startNode.f(puzzle.goal.table, CPuzzle.hTab)
        if puzzle.startNode.fScore == 0 :
            print(puzzle.startNode)
            return
        open = []
        close = []
        goal = puzzle.goal.table
        # open.append( CSpeedNode(puzzle.startNode, puzzle.startNode.state.table, puzzle.startNode.fScore, puzzle.startNode.level))
        open.append(puzzle.startNode)
        cpt = 0
        while not(len(open) == 0):
            if open[0].fScore - open[0].level ==  0 :
                return open[0]
                
            puzzle.nbOpenSelected += 1 
            tabChild = open[0].getChildren(goal)
            
            for child in tabChild:
                if child.state.table in close :
                    continue
                child.fScore = child.fSpeed(goal, CPuzzle.hSpeedTab)
                
                # child = CSpeedNode(child, child.state.table, child.fScore, child.level)
                # if child in open :
                test_open = [child.state.table == elem.state.table and child.fScore > elem.fScore for elem in open]
                if any(test_open):
                    continue
                else : 
                    bisect.insort_left(open, child)
                    if puzzle.maxOpen < len(open):
                        puzzle.maxOpen = len(open)
            close.append(open.pop(0).state.table)
        
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
    puzzle.startNode.fScore = puzzle.startNode.f(puzzle.goal.table)
    found = None
    threshold = puzzle.startNode.fScore
    while found == None :
        threshold, found = idaSearch(puzzle.startNode, threshold, puzzle)
        # on revien ici quand la tolerence sur le fScore augmente
    return found