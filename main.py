import sys
from classes.CState import CState
from classes.CNode import CNode
from classes.CPuzzle import CPuzzle

def main(argv):
    table = [8,1,4,3,0,5,7,6,2]
    state = CState(size=3, table=table)
    node = CNode(state, 0, 0)
    puzzle = CPuzzle(3)

    print(node)
    node.getChildren()

    for child in node.getChildren()

    
   
if __name__ == "__main__":
	main(sys.argv[1:])
