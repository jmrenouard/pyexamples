#!/usr/bin/python3

import random
rechercheVal=random.randint(1, 100)
for val in range(101):
    if rechercheVal == val:
        print("La valeur est: %d" % val)
        break
print ("La valeur recherchee est %d" % rechercheVal)
