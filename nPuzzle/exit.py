import sys
def usageExit():
    usage = '''Usage: python3 main.py [OPTION] [FILE]
List information about the FILEs (the current directory by default).
Option :
    -k play with arrow key
    -a chosse

            '''
    print (usage)
    sys.exit(2)

def notSolvableExit():
    print ('this puzzle is not solvable')
    sys.exit(2)
def safeExit():
    sys.exit(2)