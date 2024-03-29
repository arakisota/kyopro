"""
（解法）
・基本的にはある数をかけていって、Nを超えるタイミングでストップさせれば良い
・その他にも2の累乗であるため、ビット演算で桁数の比較で答えると簡潔にコードが書ける

（注意）
・これを対数で解くとなると、2^59と2^60あたりで誤差によって、WAしてしまう
→そのため、細かい精度を求めるときは安直に切り捨ててはいけない
"""

N = int(input())
ans = 1
cnt = 0
while ans < N:
    ans *= 2
    if ans > N:
        break
    cnt += 1

print(cnt)