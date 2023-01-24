"""
（考え方）
・数学的に考察する
→それぞれの配列の各桁をA, Bとする
→A+B=Sとなり、和は常に一定である。そのため、掛け算はA*(S-A)となるため、これらの最小を考えればいい。
→上に凸のAの二次関数になるので、最小はAorBに偏らせれば良いことがわかる
"""

N = int(input())
A = int(input())
B = int(input())

MOD = 998244353
tmp_a = [int(x) for x in list(str(A))]
tmp_b = [int(x) for x in list(str(B))]

for i in range(N):
    if tmp_a[i] > tmp_b[i]:
        tmp_a[i], tmp_b[i] = tmp_b[i], tmp_a[i]
a = int("".join(str(j) for j in tmp_a)) % MOD
b = int("".join(str(j) for j in tmp_b)) % MOD
print(a*b%MOD)