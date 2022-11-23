N, K = map(int, input().split())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

"""
座標(a, b)からK以内の正方形に入っているかどうかを調べる
(a, b)に対して、全探索をかけている
→一つを固定して、全探索する
"""
def Getscore(a, b, A, B, K):
    cnt = 0
    for i in range(N):
        if (a <= A[i] and A[i] <= a + K) and (b <= B[i] and B[i] <= b + K):
            cnt += 1
    return cnt

ans = 0
for a in range(1, 101):
    for b in range(1, 101):
        Score = Getscore(a, b, A, B, K)
        ans = max(ans, Score)

print(ans)