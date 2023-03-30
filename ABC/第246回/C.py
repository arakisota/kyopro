N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)

while K > 0:
    A.sort(reverse=True)
    if A[0] >= X:
        A[0] -= X
        ans -= X
    else:
        ans -= A[0]
        A[0] = 0
    K -= 1

print(ans)