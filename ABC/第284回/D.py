"""
N = p^2q(p, qは素数)のとき、min(p, q) <= n^(1/3)が成り立つ
→そのため、n^(1/3)の試しわりで全探索しても、TLEせずにACできる

（別解）
Pollard’s rho algorithmという高速な素因数分解アルゴリズムを用いてもできる
"""

import math
from collections import Counter

# 素因数分解を行う関数
def prime_factorization(n):
    # Counterクラスを呼び出してオブジェクト生成
    counter = Counter()
    # 素数で割り切れるかの判定
    for p in range(2, int(n ** 0.5) + 1):
        # １回割り切れるごとに+1カウントしていく
        while n % p == 0:
            counter[p] += 1
            n //= p
    # n が1より大きい数字として残っていれば、素数
    if n != 1:
        counter[n] += 1
    return counter

T = int(input())
for i in range(T):
    test = int(input())
    result = prime_factorization(test)
    for key, value in result.items():
        if value == 1:
            q = key
        if value == 2:
            p = key
    print(p, end=" ")
    print(q)