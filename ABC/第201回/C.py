"""
0000~9999までの10^4通りしかないため、適さないものを消していけばよい
"""

#解説のコード
S = input()
ans = 0
for i in range(10000):
    flag = [False]*10 #毎回リセットしている
    now = i
    for j in range(4):
        flag[now%10] = True
        now //= 10 #ここで右シフトしてる。4桁の数字をそれぞれ判定している。判定する数字を一旦Trueにしている
    flag2 = True
    for j in range(10):
        if S[j] == 'o' and not flag[j]:
            flag2 = False
        if S[j] == 'x' and flag[j]:
            flag2 = False
    ans += flag2 #flag2は0or1で認識される
print(ans)
