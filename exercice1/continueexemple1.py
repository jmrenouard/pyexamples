#!/usr/bin/python3

print ("Pair: ", end=" ")
for val in range(13):
	if val % 2 == 1:
		continue
	print (val, end=" ")

print("\nImpair: ", end=" ")
for val in range(13):
	if val % 2 == 0:
		continue
	print(val, end=" ")