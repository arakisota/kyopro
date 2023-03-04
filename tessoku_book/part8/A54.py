"""
連想配列の問題
・連想配列
→添字の制限がない配列
→Pythonの場合は辞書を使って、作成する
"""

from collections import defaultdict

Q = int(input())
score = defaultdict(int)
for i in range(Q):
    tmp = input().split()
    if tmp[0] == "1":
        score[tmp[1]] = tmp[2]
    else:
        print(score[tmp[1]])