#!/usr/bin/python3

val = 5
while val > 0:
    print("Boucle val: ", val)
    val -= 1

val = 5
while True:
  print("Boucle val: ", val)
  val -= 1
  if val < 0:
    break
