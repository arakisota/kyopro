N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
l = [0] * Q
r = [0] * Q
for i in range(Q):
    l[i], r[i] = map(int, input().split())