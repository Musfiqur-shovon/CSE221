def insertion_sorter(list1,list2):
  for i in range(len(list2)):
    for j in range(i-1,-1,-1):
      if(list2[j]<list2[j+1]):
        temp = list1[j]
        list1[j]=list1[j+1]
        list1[j+1]=temp
        temp = list2[j]
        list2[j]=list2[j+1]
        list2[j+1]=temp
      else:
        break

var = open("input3.txt","r")
out = open("output3.txt","w")
var = var.read()
var = var.split("\n")
var = var[:len(var)-1]
length = var[0]
list1 = var[1].split()
list2 = var[2].split()
array1 = []
array2 = []
for i in list1:
    array1.append(int(i))
for i in list2:
    array2.append(int(i))

insertion_sorter(array1,array2)
for i in range(0,int(length)):
    out.write(str(array1[i])+" ")