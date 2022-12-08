"""
素因数分解のコード
・一般的な素因数分解のコードは試し割り法
→素因数候補として確かめるべき値の範囲は2<= x <= √nで良い

ちなみにSympyに素因数分解をしてくれるコードがあるらしい
from sympy.ntheory import factorint
factorized = factorint(5185)
-> {5:1, 17:1, 61:1}
"""

#試し割り法
#prime_factorize(36) -> [2, 2, 3, 3]
#prime_factorize(1) -> [] 空のリスト

import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    num = collections.Counter(a) #Counter({2:3, 3:1, 5:1, 7:1})
    #num * 例 : prime_factorize(840) -> [2, 2, 3, 5, 7]
    prime_number = num.keys() #素数 dict_keys([2, 3, 5, 7])
    sisuu = num.values()    #指数 dict_values([3, 1, 1, 1])
    return prime_number, sisuu