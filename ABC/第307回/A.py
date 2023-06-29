N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    tmp = 0
    for j in range(7):
        tmp += A[i*7+j]
    ans.append(tmp)

for i in ans:
    print(i, end=" ")