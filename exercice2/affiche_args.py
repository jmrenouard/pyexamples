#!/usr/bin/python3
import sys

def affiche_args(*args):
    for i, arg in enumerate(*args):
        print("* %d) %s" % (i, arg))
if __name__ == '__main__':
    affiche_args(sys.argv)
