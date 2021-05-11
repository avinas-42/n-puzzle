import sys
from classes.CState import CState
from classes.CNode import CNode
from classes.CPuzzle import CPuzzle
from nPuzzle.parser import parsing 

def main(argv):
    print(argv[0])
    size , table = parsing(argv[0])
    table = [8,1,4,3,0,5,7,6,2]
    state = CState(size = 3, table = table)
    node = CNode(state = state, level = 0, fScore = 0)
    puzzle = CPuzzle(size = 3)

    print(node)
    print(node.getChildren())


if __name__ == "__main__":
	main(sys.argv[1:])
