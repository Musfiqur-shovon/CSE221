def selection_sorter(list):
  for i in range(len(list)-1,-1,-1):
    max_idx = i
    for j in range(0,i):
      if(list[j]>list[max_idx]):
        max_idx = j
    temp = list[max_idx]
    list[max_idx]=list[i]
    list[i]=temp


var = open("input2.txt","r")
out = open("output2.txt","w")
var = var.read()
var = var.split("\n")
var = var[:len(var)-1]
length,size = var[0].split()
list = var[1].split()
array = []
for i in list:
    array.append(int(i))
selection_sorter(array)
for i in range(0,int(size)):
    out.write(str(array[i])+" ")