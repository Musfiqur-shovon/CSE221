input = open("task2_input.txt","r")
lines = input.readlines()
n = lines.pop(0)
arr1 = [int(n[0])]
arr2 = [int(n[2])]
list1 = []
list2 = []
for line in lines:
    l = line.split()
    list1.append(int(l[0]))
    list2.append(int(l[1]))

def insertion_sorter(list2, list1):
    for i in range(len(list1)):
        for j in range(i - 1, -1, -1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
                temp = list2[j]
                list2[j] = list2[j + 1]
                list2[j + 1] = temp
            else:
                break

insertion_sorter(list1, list2)

array1 = [0] * arr2[0]
count = 0
for i in range(len(list1)):
    if array1[0] == 0:
        array1[0] = list2[i]
        count += 1
    elif array1[1] == 0:
        count += 1
        array1[1] = list2[i]
    elif array1[0] <= list1[i]:
        array1[0] = list2[i]
        count += 1
    elif array1[1] <= list1[i]:
        array1[1] = list2[i]
        count += 1

print(count)
