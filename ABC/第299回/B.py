N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

cnt = 0
win = -1
val = 0
for i in range(N):
    if C[i] == T:
        cnt += 1
        if val < R[i]:
            win = i+1
            val = R[i]

if cnt > 0:
    print(win)
else:
    win = 1
    val = R[0]
    for i in range(1, N):
        if C[i] == C[0]:
            if val < R[i]:
                win = i+1
                val = R[i]

    print(win)