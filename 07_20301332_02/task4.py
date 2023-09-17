def mergeSorter(list):
    if len(list) > 1:
        mid = len(list) // 2
        leftlist = list[:mid]
        rightlist = list[mid:]
        mergeSorter(leftlist)
        mergeSorter(rightlist)
        i = 0
        j = 0
        k = 0
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                list[k] = leftlist[i]
                i = i + 1
            else:
                list[k] = rightlist[j]
                j = j + 1
            k = k + 1
        while i < len(leftlist):
            list[k] = leftlist[i]
            i = i + 1
            k = k + 1
        while j < len(rightlist):
            list[k] = rightlist[j]
            j = j + 1
            k = k + 1

var = open("input4.txt","r")
out = open("output4.txt","w")
var = var.read()
var = var.split("\n")
var = var[:len(var)-1]
length = var[0]
list = var[1].split()
array = []
for i in list:
    array.append(int(i))

mergeSorter(array)
for i in range(0,int(length)):
    out.write(str(array[i])+" ")