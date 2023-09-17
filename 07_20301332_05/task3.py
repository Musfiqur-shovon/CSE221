input = open("task3_input.txt","r")
lines = input.readlines()
n = lines.pop(0)
list1=[]
list2=[]
count=0
for line in lines:
    lin = line.split()
    if count==0:
        for i in lin:
            list1.append(i)
    elif count==1:
        for i in lin:
            for j in i:
                list2.append(j)
    count+=1

list1.sort()
array1=[]
stack=[]
countJ=0
countj=0
var=0
for i in range((len(list2))):
    if list2[i]=="J":
        array1.append(list1[var])
        stack.append(list1[var])
        countJ+= int(list1[var])
        var+=1
    elif list2[i]=="j":
        a= stack.pop()
        array1.append(a)
        countj+= int(a)

for i in array1:
    print(i,end="")
print()
print("Jack will work for",countJ,"hours")
print("Jill will work for",countj,"hours")