N, X = map(int, input().split())
A = list(map(int, input().split()))

know = set()
know.add(X)
i = 1
know_idx = X
while i <= N:
    tmp = A[know_idx-1]
    if tmp in know:
        print(i)
        break
    else:
        know.add(tmp)
        know_idx = tmp
    i += 1