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
            
            # just debug
            if cpt % 1000 == 0 or cpt == 0:
                print(len(puzzle.open))
                print(puzzle.open[0])

            cpt += 1
            puzzle.nbOpenSelected += 1 
            tabChild = puzzle.open[0].getChildren(puzzle.goal.table)
            
            for child in tabChild:
                if any(child.state.table == elem.state.table for elem in puzzle.close):
                    continue
                if any(child.state.table == elem.state.table and child.fScore > elem.fScore for elem in puzzle.open):
                    continue
                else : 
                    bisect.insort_left(puzzle.open, child)
                    if puzzle.maxOpen < len(puzzle.open):
                        puzzle.maxOpen = len(puzzle.open)
            puzzle.close.append(puzzle.open.pop(0))
        
        return None

def idaSearch(node, threshold, puzzle) :
    if node.fScore > threshold :
        return node.fScore, None
    if node.fScore - node.level == 0 :
        return node.fScore, node
    fmin = sys.maxsize

    puzzle.nbOpenSelected += 1
    for child in node.getChildren(puzzle.goal.table) :
        # on verifie que le daddy du daddy (node.daddy) nest pas le child
        if  node.daddy != None and child.state.table == node.daddy.state.table :
            continue
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

# tentative rater de ne pas reprendre au debute ça fonctionne mais c'est lent
# mais c'est surment possible de le coder mieux
def idaSearchChild(node, threshold, puzzle) :
    node.fScore = node.f(puzzle.goal.table)
    if node.fScore > threshold :
        return node.fScore, None
    if node.fScore - node.level == 0 :
        return node.fScore, node
    fmin = sys.maxsize
    if len(node.children) > 0 :
        children = []
        getAllLastChild(node, children)
        puzzle.maxOpen += 1
        for child in children :
            if  node.daddy != None and child.state.table == node.daddy.state.table :
                continue
            node.children.append(child)
            puzzle.nbOpenSelected += 1
            temp, found = idaSearchChild(child, threshold, puzzle)
            if found != None :
                return temp, found
            if temp < fmin :
                fmin = temp
    else :
        
        for child in node.getChildren(puzzle.goal.table) :
            if  node.daddy != None and child.state.table == node.daddy.state.table :
                continue
            node.children.append(child)
            temp, found = idaSearchChild(child, threshold, puzzle)
            if found != None :
                return temp, found
            if temp < fmin :
                fmin = temp
    return fmin, None

def getAllLastChild(node, children) :
    for child in node.children :
        if len(child.children) == 0 :
            children.append(child)
        else : 
            getAllLastChild(child, children)