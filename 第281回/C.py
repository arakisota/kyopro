N, T = map(int, input().split())
A = list(map(int, input().split()))

sum_a = sum(A)
T_1 = T % sum_a
count = 0
for i in range(N):
    count = i+1
    temp = T_1
    T_1 -= A[i]
    if T_1 < 0:
        print(count, end=" ")
        print(temp)
        break

if T_1 > 0:
    print(count+1, end=" ")
    print(temp)
