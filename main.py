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
    hFunc = hManhattan
    state = CState(size, table = table)
    node = CNode(state = state, level = 0, fScore = 0, hFunc = hFunc )
    puzzle = CPuzzle(size, node)

    if not isSolvable(state, puzzle.goal) :
        notSolvableExit()

    for a, o in optlist :
        if (a == '-k'):
            puzzle.play()
    puzzle.execution(optlist)
    
if __name__ == "__main__":
	main(sys.argv[1:])
