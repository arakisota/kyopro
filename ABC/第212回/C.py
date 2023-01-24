"""
今回の問題は配列A, Bの順序が変わっても答えは変わらないので、先にソートしておくことで扱いやすくする。
（考え方）
・まずどちらかをソートをする
・Aiの値に近いBiとの差をそれぞれ求めて、その中で最小のものが答えになる
→二分探索でこれを求めればいい

（計算量）
・二分探索 → O(N*logN) or O(M*logM)
・AかBのsort → O(N*logN) or O(M*logM)
まとめるとO(N*logN + M*logM)で求めることができる

（コツ）
・二分探索の際に両端に番兵を入れると処理しやすくなる
→番兵とは仮想のindexに数値を入れることである。とてつもなく大きいまたは小さい数字を入れでも処理自体には影響しない。
だが、余計な条件分岐を減らすことができる
"""
import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.append(-1e18)
B.append(1e18)
B.sort()
ans = [0] * N
for i in range(N):
    idx = bisect.bisect_left(B, A[i])
    ans[i] = min(abs(A[i]-B[idx]), abs(A[i]-B[idx-1]))

print(min(ans))