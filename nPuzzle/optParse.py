import getopt
from .exit import usageExit 

def optParse(argv):
    try:
        optlist, argv = getopt.getopt(argv, 'kma:h:g:')
    except getopt.GetoptError:
        usageExit()
    if (len(argv) < 1):
        usageExit()
    return optlist, argv
