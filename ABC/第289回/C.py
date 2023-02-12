import itertools
N, M = map(int, input().split())
C = [0] * M
a = []
for i in range(M):
    C[i] = int(input())
    a.append(list(map(int, input().split())))

num = [i for i in range(1, N+1)]
S = list(itertools.product([0, 1], repeat=M))
cnt = 0
for i in range(len(S)):
    tmp = set()
    for j in range(len(S[i])):
        if S[i][j] == 1:
            tmp = tmp | set(a[j])
    if len(tmp) == N:
        cnt += 1

print(cnt)