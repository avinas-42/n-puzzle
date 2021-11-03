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

def execution(puzzle, search) :
        elem = None
        elem = searching(puzzle, search)
        if (elem == None) : 
            print('no result')
            safeExit()
        if (elem) :
            while elem.daddy != None:
                print(elem)
                puzzle.nbstep += 1
                elem = elem.daddy
        print(puzzle.startNode)

def main(argv):
    size , table, optlist = parsing(argv)
    goal = 0
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
    puzzle = CPuzzle(size, node, hTab = hTab, hSpeedTab = hSpeedTab, goal)
    if not isSolvable(state, puzzle.goal) :
        notSolvableExit()

    search = Search.ASTAR
    for a, o in optlist :
        if (a == '-k'):
            puzzle.play()
            safeExit()
        if (a == '-a' and o == 'ida'):
            search = Search.IDA
        elif (a == '-a' and o == 'greedy') :
            search = Search.GREEDY
        if (a == '-a' and o == 'uniform'):
            search = Search.UNIFORM
    execution(puzzle, search)
    print(search.name)
    print('number of step : ' + str(puzzle.nbstep))
    print('complexity in time : ' + str(puzzle.nbOpenSelected))
    print('complexity in size : ' + str(puzzle.maxOpen))
if __name__ == "__main__":
	main(sys.argv[1:])
