"""
文字列のハッシュの問題
→文字列を比較すると、1文字ずつ確認する必要がある
→文字列とクエリの分の計算が必要 → O(NQ) = 4 * 10^10でTLEする

（ハッシュ値での比較）
→文字列をN進法で置き換える
→ただ数が大きくなりがちだから、適当素数で割った余りを取ることが多い
→事前にハッシュ値を用意しておく
→S[l, r] = Hr - B^r-l-1 * Hl-1

（問題点）
・適当な素数の余りを取るため、ハッシュ衝突が起こる
→素数の値を大きくするしかない（実用上はほぼこれでいける）
→それでも、ケースによってはダメな場合が存在する→その時は複数の素数を使って、全て一致すれば同じとする方法をとる。
"""
N, Q = map(int, input().split())
S = input()
queries = [ list(map(int, input().split())) for i in range(Q) ]
T = list(map(lambda c: ord(c) - ord('a') + 1, S))
MOD = 2147483647
power100 = [ None ] * (N + 1)
power100[0] = 1
for i in range(N):
	power100[i + 1] = power100[i] * 100 % MOD

H = [ None ] * (N + 1)
H[0] = 0
for i in range(N):
	H[i + 1] = (H[i] * 100 + T[i]) % MOD

def hash_value(l, r):
	return (H[r] - H[l - 1] * power100[r - l + 1]) % MOD

for a, b, c, d in queries:
	hash1 = hash_value(a, b)
	hash2 = hash_value(c, d)
	if hash1 == hash2:
		print("Yes")
	else:
		print("No")