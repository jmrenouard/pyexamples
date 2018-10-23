#!/usr/bin/python3

def dit_bonjour():
    print('Bonjour !')

def dit_10_fois_bonjour():
    for i in range(0, 10):
        print(i+1,")", end=" ")
        dit_bonjour()

print("Appel a dit_bonjour(): ")
dit_bonjour()
print("="*80)
print("Appel a dit_10_fois_bonjour(): ")
dit_10_fois_bonjour()