file = open("input.txt","r")
numbers = [[] for i in range(0,len(file.readline())-1)]
for line in file:
    for i in range(0,len(line)-1):
        numbers[i].append(line[i])
#print(numbers)
gamma = ""
epsilon = ""
for i in numbers:
    gamma += str(max(set(i), key=i.count))
    epsilon += str(min(set(i), key=i.count))

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print("Answer:", gamma*epsilon)
