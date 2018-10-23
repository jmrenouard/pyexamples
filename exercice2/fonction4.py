#!/usr/bin/python3
import random
from functools import partial


def donne_nombre_entre(min=1, max=100):
    print("Selection aleatoire entre %d et %d" % (min, max))
    return random.randint(min, max)


donne_nombre_100_300 = partial(donne_nombre_entre, 100, 300)

for i in range(0, 10):
    print(i+1,")", donne_nombre_100_300())
