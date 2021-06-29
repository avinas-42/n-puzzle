import sys
from Classes.CState import CState
from Classes.CNode import CNode
from Classes.CPuzzle import CPuzzle
from nPuzzle.parser import parsing 
from nPuzzle.exit import * 
from nPuzzle.UtilsSearch.heuristics import *
from nPuzzle.isSolvable import isSolvable

def main(argv):
    size , table, optlist = parsing(argv)
    if (size == -1):
        #table vaut une erreur ici
        print(table)
        usageExit()
    hTab = [hManhattan]
    for a, o in optlist :
        if (a == '-h' and "li" in o):
            hTab.append(hLinearConflict)
        if (a == '-h' and "co" in o):
            if size == 3 :
                hTab.append(hCornerConflictEight)
            else : 
                hTab.append(hCornerConflict)
    
    state = CState(size, table = table)
    node = CNode(state = state, level = 0, fScore = 0, hTab = hTab )
    puzzle = CPuzzle(size, node)
    # print(puzzle.goal)
    if size == 3 :
        if not isSolvable(state, puzzle.goal) :
            notSolvableExit()
        
    # print(hLinehaTtan(node, state.table, puzzle.goal.table))
    # print(hManhattan(node, state.table, puzzle.goal.table))
    
    for a, o in optlist :
        if (a == '-k'):
            puzzle.play()
            safeExit()
    puzzle.execution(optlist)
    print('number of step : ' + str(puzzle.nbstep))
    print('complexity in time : ' + str(puzzle.nbOpenSelected))
    print('complexity in size : ' + str(puzzle.maxOpen))
if __name__ == "__main__":
	main(sys.argv[1:])
