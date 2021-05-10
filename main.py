import sys
from classes.CState import CState
from classes.CNode import CNode


def main(argv):
    table = [8,1,4,3,0,5,7,6,2]
    state = CState(size=3, table=table)
    node = CNode(state, 0, 0)
    print(node)
    print(node.getChildren())
    
   
if __name__ == "__main__":
	main(sys.argv[1:])
