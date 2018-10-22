#!/usr/bin/python3
import sys

def affiche_args(*args):
    print("Il y a %d argument(s)" % len(*args))
    for i, arg in enumerate(*args):
        print("* %d) %s" % (i+1e, arg))
if __name__ == '__main__':
    affiche_args(sys.argv)
