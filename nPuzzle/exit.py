import sys
def usageExit():
    usage = '''Usage: python3 main.py [OPTION] FILE
Option :
    -k play with arrow key.
    -a choose an algorithm: astar, greedy, uniform, ida.
    -h choose an heuristic: linear, corner. You can chosse both with -h coli
'''
    print (usage)
    sys.exit(2)

def notSolvableExit():
    print ('this puzzle is not solvable')
    sys.exit(2)
def safeExit():
    sys.exit(2)