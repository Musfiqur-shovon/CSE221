dict = {}
file = open("input.txt", "r")
lines = file.readlines()
n = int(lines[0])

lines.pop(0)
for line in lines:
    line= line.split()
    if len(line)==1:
        dict[line[0]]=list()
    else:
        dict[line[0]]= [line[1]]
        for i in range(2,len(line)):
            dict[line[0]].append(line[i])
print(dict)