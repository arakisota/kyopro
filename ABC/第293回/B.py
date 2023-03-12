N = int(input())
A = list(map(int, input().split()))
p = [i for i in range(1, N+1)]

x = set()
for i in range(N):
    if i+1 in x:
        continue
    else:
        x.add(A[i])

K = N - len(x)
X = sorted(list(set(p) - x))

print(K)
for i in X:
    print(i, end=" ")