import getopt
from .exit import usageExit 

def optParse(argv):
    try:
        optlist, argv = getopt.getopt(argv, 'ka:h:')
    except getopt.GetoptError:
        usageExit()
    if (len(argv) < 1):
        usageExit()
    return optlist, argv
