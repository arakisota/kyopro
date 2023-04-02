N, X = map(int, input().split())
A = list(map(int, input().split()))

s = set(A)
flag = False

for i in range(N):
    if A[i] + X in s:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")