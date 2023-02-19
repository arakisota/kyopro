N, K = map(int, input().split())
A = list(map(int, input().split()))

A2 = sorted(list(set(A)))[:K]
if A2[0] != 0:
    print(0)
else:
    for i in range(len(A2)):
        if A2[i] != i:
            print(i)
            break
        if i == len(A2) - 1:
            print(i+1)