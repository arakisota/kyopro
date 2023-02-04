"""
ord()はUnicodeポイントを計算する関数である。
"""

from string import ascii_lowercase

X = input()
N = int(input())
S = [0] * N
tmp = [0] * N
for i in range(N):
    tmp[i] = input()
    ans_tmp = str()
    for s in tmp[i]:
        ans_tmp += str(ascii_lowercase[X.index(s)])
    S[i] = ans_tmp
num = [i for i in range(N)]
dict_tmp = dict(zip(S, num))
anss = sorted(dict_tmp)
for ans in anss:
    print(tmp[dict_tmp[ans]])