data = input()

N, M = list(map(int, data.split()))

matrix_1 = []
for i in range(N):
    matrix_1.append(list(map(int, input().split())))

matrix_2 = []
for i in range(N):
    matrix_2.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        matrix_1[j][i] = matrix_1[j][i] + matrix_2[j][i]

for i in matrix_1:
    for j in i:
        print(j, end=" ")
    print()    

