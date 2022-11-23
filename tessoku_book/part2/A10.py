#入力
N = int(input())
A = list(map(int, input().split()))

D = int(input())
L = [None] * D
R = [None] * D

for i in range(D):
    L[i], R[i] = map(int, input().split())

#P[i]を求める
P = [None] * N
P[0] = A[0]
for i in range(1, N):
    P[i] = max(P[i-1], A[i])

#Q[i]を求める
Q = [None] * N
Q[N-1] = A[N-1]
for i in reversed(range(0, N-1)):
    Q[i] = max(Q[i+1], A[i])

#それぞれの日について考える
#P[(L[i]-1)]になっているのはindexが0から始まるから
for d in range(D):
    print(max(P[(L[d]-1)-1], Q[(R[d]+1)-1]))