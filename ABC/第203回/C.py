from collections import defaultdict

N, K = map(int, input().split())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

#事前に村人がいる場所ともらえるお金を整理する
get_m = defaultdict(int)
for j in range(N):
    get_m[A[j]] += B[j]

"""
村人がいるところ以外は動作が同じだから計算を省くようにする
"""
now = 0

for key in sorted(get_m.keys()):
    dist = key - now
    if K - dist >= 0:
        K -= dist
        K += get_m[key]
        now += dist
    else:
        break

print(now + K)