"""
考察のポインt
・どのような配列を持つか
・配列の遷移→前の結果からどう計算するか
・入れるのどこが求めるべき答えになるのか
"""

H, W = map(int, input().split())
c = [None] * H

for i in range(H):
    c[i] = input()

#動的計画法
#dp[i][j]はマス(1,1)から(i,j)まで移動する方法の数
dp = [[0] * (W+1) for i in range(H+1)]
#初期値は1
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            dp[i][j] = 1
        else:
            #ブロックになっているところを0にするために
            dp[i][j] = 0    
            #上まだは左が.であれ場合は足す
            if i >= 1 and c[i-1][j] == ".":
                dp[i][j] += dp[i-1][j]
            if j >= 1 and c[i][j-1] == ".":
                dp[i][j] += dp[i][j-1]

print(dp[H-1][W-1])