N, M = map(int, input().split())
A = [None] * M
B = [None] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())

mati_list = [[] for i in range(N)]

for i in range(M):
    mati_list[A[i]-1].append(B[i])
    mati_list[B[i]-1].append(A[i])

for i in range(N):
    mati_list[i].sort()
    print(len(mati_list[i]), end=" ")
    print(*mati_list[i])
