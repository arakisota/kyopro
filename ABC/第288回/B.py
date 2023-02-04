N, K = map(int, input().split())
S = [0] * N
for i in range(N):
    S[i] = input()

ans = sorted(S[:K])
for i in ans:
    print(i)