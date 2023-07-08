N = int(input())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input())))
#print(A)

for i in range(N):
    tmp = []
    if i == 0:
        for j in range(N):
            if j == 0:
                tmp.append(A[i+1][j])
            else:
                tmp.append(A[i][j-1])
    elif i == N-1:
        for j in range(N):
            if j == N-1:
                tmp.append(A[i-1][j])
            else:
                tmp.append(A[i][j+1])
    else:
        for j in range(N):
            if j == N-1:
                tmp.append(A[i-1][j])
            elif j == 0:
                tmp.append(A[i+1][j])
            else:
                tmp.append(A[i][j])
    B.append(tmp)

for i in range(N):
    ans = str()
    for val in B[i]:
        ans += str(val)
    print(ans)