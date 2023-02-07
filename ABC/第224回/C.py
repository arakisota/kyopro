"""
ただ三角形ができる条件を求めれば良い。
"""
N = int(input())
X = [0] * N
Y = [0] * N

xy = []
for i in range(N):
    X[i], Y[i] = map(int, input().split())

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (X[j] - X[i])*(Y[k] - Y[i]) - (X[k]- X[i])*(Y[j] - Y[i]):
                cnt += 1
print(cnt)