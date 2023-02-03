N, M = map(int, input().split())
S = [0] * N
T = [0] * M

cnt = 0
for i in range(N):
    temp = input()
    S[i] = temp[-3:]
for j in range(M):
    T[j] = input()

for s in S:
    if s in set(T):
        cnt += 1
print(cnt)