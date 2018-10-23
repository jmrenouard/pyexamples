#!/usr/bin/python3

def multiply(*args):
    z = 1
    for num in args:
	    z *= num
    print(z)

multiply(4, 5)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(param_1="requin", param_2=5.678, param_3=True)
