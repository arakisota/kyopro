"""
二次元配列のDPを使う問題
（考え方）
dp[i][j] : Sのi文字目までを使って、chokudaiのj文字目を選択する方法
→簡単なテストケースを表にするとわかりやすい
（解法のイメージ）
chokudaiを作るためには、chokudaが必要
→choukudaを作るためには、chokudが必要
...
→chを作るためには、cが必要となる
（計算量）
dpをするためO(S*8)となる
"""

S = input()
T = "chokudai"
#dp[i][j] : Sのi文字目までを使って、chokudaiのj文字目を選択する方法
dp = [[0]*9 for i in range(len(S)+1)]
for i in range(len(S)+1):
    for j in range(9):
        if j == 0: #0文字目は下線を全く引いていないので1通り
            dp[i][j] = 1
        elif i == 0: #Sの0文字を使うだから、0通り
            dp[i][j] = 0
        elif S[i-1] != T[j-1]: #S[i]!=T[j]よりパターンの数変わらない
            dp[i][j] = dp[i-1][j]
        else: #Sのi文字目に下線を引くパターンと引かないパターンで合計する
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

MOD = pow(10, 9) + 7
print(dp[len(S)][8] % MOD)

"""以下、別解"""
#dp[i]:i文字目までにないが何通り作れるかを考える
from collections import Counter

T = "*chokudai" #これを0番目をわかりやすいように*で適当に入れておく
dp = Counter()
dp["*"] = 1
for char in S:
    if char in T:
        char_prev = T[T.index(char)-1] #charの前の文字
        dp[char] += dp[char_prev]
        dp[char] %= MOD #常に割っておくことでオーバーフロー対策になる
print(dp["i"])