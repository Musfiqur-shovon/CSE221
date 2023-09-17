
a = [[1,2,3],[1,3,4],[2,4,1]]
b = [[4,7,1,],[9,2,1],[6,2,1]]

num = len(a)
c = [[0 for i in range(num)]for j in range(num)]
for i in range(num):
    for j in range(num):
        for k in range(num):
            c[i][j] += a[i][k]*b[k][j]

for i in c:
    for j in i:
        print(j,end=" ")
    print()
















