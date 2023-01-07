T = int(input())
test = [None] * T

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    for j in range(N):
        A[j] = A[j] % 2
    print(sum(A))