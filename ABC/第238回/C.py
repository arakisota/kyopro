"""
(1+n)*n/2
1~9 -> 9
10~99 -> 90
100~999 -> 900
1000~9999 -> 9000
"""
def f(N):
    return int((1+N)*N/2)

N = int(input())
MOD = 998244353

Q = len(str(N))
amari = N % 10
ans = 0
for i in range(1, Q+1):
    ans += f(9*pow(10, i)) % MOD