N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
judge = 1
for i in range(M):
    if B[i] in set(A):
        ans.append(B[i])
        A.pop(A.index(B[i]))
    else:
        judge = 0
        break
if judge == 0:
    print("No")
else:
    print("Yes")