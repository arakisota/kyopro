from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []
C += A
C += B

num = defaultdict()
num2 = defaultdict()
C.sort()
for i in range(len(C)):
    num[i] = C[i]

ans = sorted(num.items(), key = lambda a : a[1])
for a, b in ans:
    num2[b] = a

ans1 = []
ans2 = []
for a in A:
    ans1.append(num2[a]+1)
for b in B:
    ans2.append(num2[b]+1)

print(*ans1)
print(*ans2)