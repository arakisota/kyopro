N, W = map(int, input().split())
A = list(map(int, input().split()))

num = set()
for i in range(N):
    tmp = A[i]
    if tmp <= W:
        num.add(tmp)
    for j in range(i+1, N):
        tmp = A[i] + A[j]
        if tmp <= W:
            num.add(tmp)
        for k in range(j+1, N):
            tmp = A[i] + A[j] + A[k]
            if tmp <= W:
                num.add(tmp)

print(len(num))