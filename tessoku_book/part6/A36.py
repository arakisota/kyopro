"""
偶奇に考える問題
→偶数マスと奇数マスで色を塗り分けるとわかりやすい
→最短経路から余ったところは近場で行ったり来たりさせれば良い
"""
N, K = map(int, input().split())

if 2 * (N-1) <= K:
    if K % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")