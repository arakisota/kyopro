H, W = map(int, input().split())
A = []
B = []
for i in range(H):
    A.append(input())

for i in range(H):
    B.append(input())

def shift(H, A, i):
    shift1 = []
    #横シフト
    for j in range(H):
        tmp = A[j][i:] + A[j][:i]
        shift1.append(tmp)
    return shift1

FLAG = False
for i in range(W):
    shift1 = shift(H, A, i)
    tr_shift1 = [list(x) for x in zip(*shift1)]
    for j in range(H):
        shift2 = shift(W, tr_shift1, j)
        tr_shift2 = [list(x) for x in zip(*shift2)]
        ans = []
        for k in range(H):
            ans_2 = str()
            for l in range(W):
                ans_2 += tr_shift2[k][l]
            ans.append(ans_2)
        if ans == B:
            FLAG = True
            break

if FLAG:
    print("Yes")
else:
    print("No")