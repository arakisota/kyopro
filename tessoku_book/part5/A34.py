"""
Groundby数 : ゲーム盤面の状態
山iの時のGroundby数をGiとした時
G1 XOR G2 XOR G3 XOR ... XOR GN = 0 -> 後手必勝
G1 XOR G2 XOR G3 XOR ... XOR GN ≠ 0 -> 先手必勝
"""
#入力

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

#groungby[i] : 石がi個の時のGroundby
#Transit[i] : Groundby数がiとなるような遷移ができるか
groundby = [None] * 100001
for i in range(100001):
    Transit = [False, False, False]
    if i >= X:
        Transit[groundby[i-X]] = True
    if i >= Y:
        Transit[groundby[i-Y]] = True

    if Transit[0] == False:
        groundby[i] = 0
    elif Transit[1] == False:
        groundby[i] == 1
    else:
        groundby[i] = 2

#出力
XOR_Sum = 0
for i in range(N):
    XOR_Sum = (XOR_Sum ^ groundby[A[i]])
if XOR_Sum >= 1:
    print("First")
else:
    print("Second")