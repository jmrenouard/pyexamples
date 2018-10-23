#!/usr/bin/python3

for n in range(15):
    if n == 0:
        print("%d est zero." % n)
    elif n == 1 or n == 9 or n == 4:
        print("%d is a perfect square" % n)
    elif n == 2:
        print("%d is an even number" % n)
    elif n == 3 or n == 5 or n == 7:
        print("%d is a prime number" % n)
