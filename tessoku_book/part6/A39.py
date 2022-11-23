"""
貪欲法：1ステップ先だけを考えた時の最善手を選び続ける手法
"""
N = int(input())

A = []

for i in range(N):
    #rに終了時刻、lに開始時刻を入れてることに注意
    l, r = map(int, input().split())
    A.append([r, l])  #ここで逆になってることに注意

A.sort()

#常に終了時刻が早いものを選ぶ
Current_time = 0
Answer = 0
for i in range(N):
    #終了時刻が早いものから貪欲に取っていく(Current_timeが今見てる映画の終了時刻になっている)
    if Current_time <= A[i][1]:
        Current_time = A[i][0]
        Answer += 1

print(Answer)        