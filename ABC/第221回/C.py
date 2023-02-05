"""
（コツ）
Nの制約が10^9だが、桁数なので高々10桁しかない。かつ、2グループにそれぞれの数字を分けるだけなので、組み合わせは2^10=1024通りしかない。
そのため、全探索で調べてしまえばいい。
→ビット全探索
"""

import copy
N = list(input())
N.sort(reverse=True)

n1 = N[0]
n2 = N[1]
for i in range(2, len(N)):
    copy1 = copy.copy(n1)
    copy2 = copy.copy(n2)
    copy1+=N[i]
    copy2+=N[i]
    if int(copy1)*int(n2) > int(n1)*int(copy2):
        n1 += N[i]
    else:
        n2 += N[i]

print(int(n1)*int(n2))