input = open("task1_input.txt","r")
lines = input.readlines()
n = lines.pop(0)
lst1 = []
lst2 = []
for line in lines:
    lin = line.split()
    lst1.append(int(lin[0]))
    lst2.append(int(lin[1]))

def insertion_sorter(lst2, lst1):
    for i in range(len(lst1)):
        for j in range(i - 1, -1, -1):
            if (lst1[j] > lst1[j + 1]):
                temp = lst1[j]
                lst1[j] = lst1[j + 1]
                lst1[j + 1] = temp
                temp = lst2[j]
                lst2[j] = lst2[j + 1]
                lst2[j + 1] = temp
            else:
                break

insertion_sorter(lst1, lst2)

selected = list()
p = list()
count = 0
f=0
for i in range(len(lst1)):
    if len(selected) == 0:
        f = lst2[i]
        selected.append(lst2[i])
        p.append(lst1[i])
        count += 1
    else:
        if lst1[i] >= f:
            count += 1
            f = lst2[i]
            selected.append(lst2[i])
            p.append(lst1[i])
print(count)
for i in range(len(selected)):
    print(f"{p[i]} {selected[i]}")