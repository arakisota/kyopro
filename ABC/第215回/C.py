"""
（解法）
・文字列の数が多くないため、全ての組み合わせを列挙して、それをソートしてK番目を答えれば良い
（コツ）
itertoolsを使えば、順列や組み合わせが簡単に表現できるため、使い慣れるようにする
"""

import itertools

S, K = map(str, input().split())
K = int(K)
ans = str()

s_list = list(S)
s_ans = list(itertools.permutations(s_list))
ans_sort = sorted(set(s_ans))
for s in ans_sort[K-1]:
    ans += s
print(ans)