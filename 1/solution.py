#!/bin/python3
file = open("input.txt","r")
old = None
biggerCount = 1
for line in file:
    if not old:
        old = line.strip()
    if line.strip() > old:
        print(line.strip(),"+1")
        biggerCount += 1
    else:
        print(line.strip(),"-")
    old = line.strip()
print(biggerCount)    
