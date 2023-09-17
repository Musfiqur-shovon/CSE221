def bubble_sorter(list):
    for i in range(len(list)-1,-1,-1):
      loop = False
      for j in range(0,i):
          if list[j]>list[j+1]:
              temp = list[j]
              list[j]=list[j+1]
              list[j+1]=temp
              loop = True
      if loop == False:
            break

var = open("input1.txt","r")
out = open("output1.txt","w")
var = var.read()
var = var.split("\n")
var = var[:len(var)-1]
length = var[0]
list = var[1].split()
array = []
for i in list:
    array.append(int(i))

bubble_sorter(array)
for i in range(0,int(length)):
    out.write(str(array[i])+" ")

"""
If we want to find out the best case, you have to use less loop. 
here is an extra loop variable for controlling the loop till n times. 
So, now the time complexity of the code is theta(n).
""" 