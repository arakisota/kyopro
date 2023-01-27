"""
（コツ）
・直線の場合と円形の場合で異なるため、このあたりの考察を入れる
→円周だと直線でいう最後尾から先頭に宝石が渡されるパターンも考慮する必要がある
→2周すれば、これを簡単に処理することができる
"""

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = [1e18] * N
for i in range(2*N):
    if i == 0:
        ans[i] = T[i]
    else:
        ans[(i+1) % N] = min(ans[i % N] + S[i % N], T[(i+1) % N])

for i in ans:
    print(i)