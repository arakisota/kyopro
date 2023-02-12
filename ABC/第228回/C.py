import copy

N, K = map(int, input().split())
P = []
num = [i for i in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    P.append(sum(tmp))
score_sorted = sorted(P, reverse=True)
K_score = score_sorted[K-1]

for i in range(N):
    if K_score <= P[i] + 300:
        print("Yes")
    else:
        print("No")