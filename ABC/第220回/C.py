N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_a = sum(A)
q = X // sum_a
X -= sum_a * q
ans = q*N
for a in A:
    ans += 1
    X -= a
    if X < 0:
        break
print(ans)