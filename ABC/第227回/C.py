"""
（式変形）
A <= N ** 1/3 -> BC <= N/A -> B <= N/A ** 1/2 -> B <= C <= N/AB
(コツ)
a <= N**1/3より、a*a*a <= Nの方が誤差が出ずに、条件分岐できる
"""

N = int(input())

cnt = 0
num = int(pow(N, 1/3))

for a in range(1, N+1):
    if pow(a, 3) > N:
        break
    for b in range(a, N+1):
        if a * b * b > N:
            break
        tmp = N // a // b
        cnt += tmp - b + 1
print(cnt)