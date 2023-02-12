N = int(input())
L = [0] * N
a = set()

for i in range(N):
    L[i], *tmp = list(map(int, input().split()))
    a.add(tuple(tmp))

print(len(a))