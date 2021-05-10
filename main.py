import sys
from classes.CState import CState

def main(argv):
    table = [8,1,4,3,0,5,7,6,2]
    state = CState(size=3, table=table)
    print(state)
    state.swap(1,1,2,1)
    print (state)


if __name__ == "__main__":
	main(sys.argv[1:])
