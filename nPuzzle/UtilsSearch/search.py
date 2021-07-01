import sys
import bisect
from collections import deque
def aStar(puzzle) :
        puzzle.startNode.fScore = puzzle.startNode.f(puzzle.goal.table)
        if puzzle.startNode.fScore == 0 :
            print(puzzle.startNode)
            return
        open = []
        close = []
        goal = puzzle.goal.table
        open.append(puzzle.startNode)
        # cpt = 0
        while not(len(open) == 0):
            if open[0].fScore - open[0].level ==  0 :
                return open[0]
            
            # just debug
            # if cpt % 1000 == 0 or cpt == 0:
            #     print(len(open))
            #     print(open[0])

            # cpt += 1
            puzzle.nbOpenSelected += 1 
            tabChild = open[0].getChildren(goal)
            
            for child in tabChild:
                if any(child.state.table == elem.state.table for elem in close):
                    continue
                child.fScore = child.fSpeed(goal)
                if any(child.state.table == elem.state.table and child.fScore > elem.fScore for elem in open):
                    continue
                else : 
                    bisect.insort_left(open, child)
                    if puzzle.maxOpen < len(open):
                        puzzle.maxOpen = len(open)
            close.append(open.pop(0))
        
        return None

def idaSearch(node, threshold, puzzle) :
    if node.daddy != None : 
        node.fScore = node.fSpeed(puzzle.goal.table)
    else :
        node.fScore = node.f(puzzle.goal.table)
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

# tentative rater de ne pas reprendre au debut ça fonctionne mais c'est lent
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