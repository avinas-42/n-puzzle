import getopt, sys
from .exit import usageExit 

def optParse(argv):
    try:
        optlist, argv = getopt.getopt(argv, 'ksfa:')
    except getopt.GetoptError:
        usageExit()
    if (len(argv) < 1):
        usageExit()
    return optlist, argv
