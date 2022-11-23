"""
答えは絶対にXXを超えないといった上限値を考えることによって、解放の見通しがよくなる
"""
D, N = map(int, input().split())
L = [0] * N
R = [0] * N
H = [0] * N

for i in range(N):
    L[i], R[i], H[i] = map(int, input().split())

LIM = [24] * (D+1)
for i in range(N):
    for j in range(L[i], R[i]+1):
        LIM[j] = min(LIM[j], H[i])

print(sum(LIM[1:]))