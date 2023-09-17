# Task 02
import numpy
def LCS(X, Y, Z):
    m= len(X) + 1
    n = len(Y) + 1
    o = len(Z) + 1
    C = numpy.zeros((m, n, o))

    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):

                if Y[j - 1] == X[i - 1] == Z[k - 1]:
                    C[i][j][k] = (C[i - 1][j - 1][k - 1]) + 1

                else:

                    if C[i - 1][j][k] >= C[i][j - 1][k]:
                        temp = C[i - 1][j][k]

                        if temp >= C[i][j][k - 1]:
                            C[i][j][k] = temp

                        else:
                            C[i][j][k] = C[i][j][k - 1]

                    else:
                        temp = C[i][j - 1][k]

                        if temp >= C[i][j][k - 1]:
                            C[i][j][k] = temp

                        else:
                            C[i][j][k] = C[i][j][k - 1]

    return int(C[len(X)][len(Y)][len(Z)])



# x,y,z can be taken from user as well.
x ="abbcdab"
y= "daccbadb"
z= "abccdaab"

print(LCS(x, y, z))