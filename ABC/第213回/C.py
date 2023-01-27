"""
行と列が互いに独立なので、それぞれAの中の何番目、Bの中の何番目かを考えればよい
→座標圧縮(座圧)をする
"""

H, W, N = map(int, input().split())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

#座標圧縮
cp_a = sorted(list(set(A)))
cp_b = sorted(list(set(B)))

ans_a = {x: i+1 for i, x in enumerate(cp_a)} #ソートされた状態でvalueに対して、indexが割り振られる
ans_b = {y: j+1 for j, y in enumerate(cp_b)}

for k in range(N):
    print(ans_a[A[k]], ans_b[B[k]])