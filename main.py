import sys
from Classes.CState import CState
from Classes.CNode import CNode
from Classes.CPuzzle import CPuzzle
from nPuzzle.parser import parsing 
from nPuzzle.usageExit import usageExit 

def main(argv):
    size , table, optlist = parsing(argv)
    if (size == -1):
        #table vaut une erreur ici
        print(table)
        usageExit()

    state = CState(size, table = table)
    node = CNode(state = state, level = 0, fScore = 0)
    puzzle = CPuzzle(size, node)
    for a, o in optlist : 
        if (a == '-k'):
            puzzle.play()
    

    puzzle.execution()
    

if __name__ == "__main__":
	main(sys.argv[1:])
