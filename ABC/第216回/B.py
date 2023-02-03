N = int(input())
S = [None] * N
T = [None] * N
name = [None] * N
for i in range(N):
    S[i], T[i] = map(str, input().split())
    name[i] = S[i] + "-" + T[i]

if len(set(name)) == N:
    print("No")
else:
    print("Yes")