N = int(input())
A = list(map(int, input().split()))

if len(set(A)) == N:
    print("Yes")
else:
    print("No")