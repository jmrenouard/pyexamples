#!/usr/bin/python3

import random
def donne_nombre_entre_1_et_100():
    return random.randint(1, 100)

for i in range(0, 10):
    print(i+1,")",donne_nombre_entre_1_et_100())

