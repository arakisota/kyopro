N = int(input())
X = list(map(int, input().split()))

X_S = sorted(X)

print(sum(X_S[N:4*N]) / (3*N))