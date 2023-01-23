N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

temp = [0] * N
for i in range(len(A)):
    if P-1 <= i <= Q-1:
        temp[i] = A[R-P+i]
    elif R-1 <= i <= S-1:
        temp[i] = A[P-R+i]
    else:
        temp[i] = A[i]
print(*temp)