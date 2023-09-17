# Task 01
PUBG = {'Y': "Yasnaya", 'R': "Rozhok",'S': "School", 'P': "Pochinki",'F': "Farm", 'M': "Mylta",'H': "Shelter", 'I': "Prison"}


def LCS(X, Y):
    m= len(X) + 1
    n=len(Y) + 1
    C, T = [], []

    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(0)
        C.append(temp)

    for i in range(m):
        temp = []
        for j in range(n):
            temp.append('N')
        T.append(temp)

    for i in range(1, m):
        for j in range(1, n):

            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                T[i][j] = 'd'

            elif C[i - 1][j] >= C[i][j - 1]:
                C[i][j] = C[i - 1][j]
                T[i][j] = 'u'

            else:
                C[i][j] = C[i][j - 1]
                T[i][j] = 'l'

    r= m - 1
    c= n - 1

    seq = []

    while T[r][c] != 'N':
        if T[r][c] == 'd':
            seq.append(X[c - 1])
            r -= 1
            c -= 1

        elif T[r][c] == 'l':
            c -= 1

        else:
            r -= 1

    seq.reverse()

    for i in seq:
        print(PUBG[i], end=' ')
    print()
    return seq


N = 8
x, y = "YRSPFMHI", "YPSRFMHI"

a = ((len(LCS(x, y)) * 100) / N)
print(f"Correctness of prediction: {int(a)}%")






