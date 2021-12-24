file = open("input.txt","r")
depth = 0
forward = 0
aim = 0
for line in file:
    instruction = line.strip().split()
    if instruction[0] == "forward":
        forward += int(instruction[1])
        depth += (int(instruction[1])*aim)
    if instruction[0] == "down":
        aim += int(instruction[1])
    if instruction[0] == "up":
        aim -= int(instruction[1])
print("Forward:", forward)
print("Depth:", depth)
print("Answer:", forward*depth)
