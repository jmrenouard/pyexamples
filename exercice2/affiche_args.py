#!/usr/bin/python3
import sys

def afficheargs(*args):
    print("Il y a %d argument(s)" % len(*args))
    for i, arg in enumerate(*args):
        print("* %d) %s" % ((i + 1e), arg))
if __name__ == '__main__':
    afficheargs(sys.argv)
