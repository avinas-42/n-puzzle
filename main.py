import sys
from Classes.CState import CState
from Classes.CNode import CNode
from Classes.CPuzzle import CPuzzle
from nPuzzle.parser import parsing 
from nPuzzle.exit import * 
from nPuzzle.isSolvable import isSolvable
from nPuzzle.UtilsSearch.heuristics import *
from nPuzzle.UtilsSearch.searchEnum import Search
from nPuzzle.UtilsSearch.search import searching
from nPuzzle.front.front import front

def display(elem, puzzle, search) :
    
    if (elem == None) : 
        print('no result')
        safeExit()
    if (elem) :
        while elem.daddy != None:
            puzzle.nbstep += 1
            print(elem)
            elem = elem.daddy
    print(puzzle.startNode)
    print(search.name)
    print('number of step : ' + str(puzzle.nbstep))
    print('complexity in time : ' + str(puzzle.nbOpenSelected))
    print('complexity in size : ' + str(puzzle.maxOpen))

def execution(puzzle, search, mSearch, tabSearch, goal, visu) :
    if mSearch and len(tabSearch) > 0:
        for oneSearch in tabSearch:
            elem = searching(puzzle, oneSearch)
            display(elem, puzzle, oneSearch)
            puzzle = CPuzzle(puzzle.size, puzzle.startNode, goal, puzzle.hTab, puzzle.hSpeedTab)
    else :
        elem = searching(puzzle, search)
        display(elem, puzzle, search)
        if visu:
            front(elem, puzzle)
        
def main(argv):
    size , table, optlist = parsing(argv)
    goal = 0
    visu = False
    if (size == -1):
        #table vaut une erreur ici
        print(table)
        usageExit()
    hSpeedTab = [hManhattanOneTile]
    hTab = [hManhattan]    
    for a, o in optlist :
        if (a == '-h' and "d" in o):
            hSpeedTab = [hDumb]
            hTab = [hDumb]
        if a == '-g':
            goal = int(o)
        if a == '-v':
            visu = True
    for a, o in optlist :
        if (a == '-h' and "li" in o):
            hTab.append(hLinearConflict)
            hSpeedTab.append(hLinearConflictOneTile)
        if (a == '-h' and "co" in o):
            if size == 3 :
                hTab.append(hCornerConflictEight)
                hSpeedTab.append(hCornerConflictEight)
            else : 
                hTab.append(hCornerConflict)
                hSpeedTab.append(hCornerConflict)
    
    state = CState(size, table = table)
    node = CNode(state = state, level = 0, fScore = 0)
    puzzle = CPuzzle(size, node, goal, hTab = hTab, hSpeedTab = hSpeedTab)
    if not isSolvable(state, puzzle.goal) :
        notSolvableExit()
    mSearch = False
    search = Search.IDA
    for a, o in optlist :
        if a == '-m':
            mSearch = True
            break

    tabSearch = []
    if mSearch:
        for a, o in optlist :
            if (a == '-a' and o == 'astar'):
                tabSearch.append(Search.ASTAR)
            if (a == '-a' and o == 'ida'):
                tabSearch.append(Search.IDA)
            if (a == '-a' and o == 'greedy') :
                tabSearch.append(Search.GREEDY)
            if (a == '-a' and o == 'uniform'):
                tabSearch.append(Search.UNIFORM)

    for a, o in optlist :
        if (a == '-k'):
            puzzle.play()
            safeExit()
        if (a == '-a' and o == 'astar'):
            search = Search.ASTAR
        elif (a == '-a' and o == 'greedy') :
            search = Search.GREEDY
        if (a == '-a' and o == 'uniform'):
            search = Search.UNIFORM
    execution(puzzle, search, mSearch, tabSearch, goal, visu)
    
if __name__ == "__main__":
	main(sys.argv[1:])
