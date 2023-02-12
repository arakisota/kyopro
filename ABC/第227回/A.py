N, K, A = map(int, input().split())

s = K % N
if N == 1:
    print(1)
elif A + s - 1 > N:
    print(A + s - 1 - N)
else:
    print(A + s - 1)