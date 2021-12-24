#!/bin/python3
file = open("input.txt","r")
old = None
biggerCount = 0
lines = file.read().splitlines()
for i in range(0,len(lines)-2):
    isum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    print(isum)
    if not old:
        old = isum
    if isum > old:
        biggerCount +=1
    old = isum
print(biggerCount)
