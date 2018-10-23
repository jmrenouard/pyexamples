#!/usr/bin/python3

import random
def donne_nombre_entre(min=1, max=100):
    print("Selection aleatoire entre %d et %d" % (min, max))
    return random.randint(min, max)

#for i in range(0, 10):
#    print(i+1,")",donne_nombre_entre(1, i+1))


for i in range(0, 10):
    print(i+1,")", donne_nombre_entre(max=i+1, min=1))

