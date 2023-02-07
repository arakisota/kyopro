H, W = map(int, input().split())
A = []
for i in range(H):
    tmp = list(map(int, input().split()))
    A.append(tmp)

ans = 1
for i in range(H-1):
    for j in range(W-1):
        if A[i][j] + A[i+1][j+1] > A[i+1][j] + A[i][j+1]:
            ans = 0
            break
if ans == 0:
    print("No")
else:
    print("Yes")