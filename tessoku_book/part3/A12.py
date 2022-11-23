"""
答えに対して、二分探索をかけていくやり方
答えがx以下かを判定し、YesであればTrue、NoであればFalseを返す関数
"""

#答えがx以下を判定する関数
#合計を出すことで答えから二部探索する
def check(x, N, K, A):
    sum = 0 
    #これで合計を出している
    for i in range(N):
        sum += x // A[i]
    
    if sum >= K:
        return True
    return False

N, K = map(int, input().split())
A = list(map(int, input().split()))

#二分探索
LEFT = 1 #確実にTrueな値を入れる
RIGHT = 10 ** 9 #確実にFalseな値を入れる

while LEFT < RIGHT:
    Mid = (LEFT + RIGHT) // 2
    Answer = check(Mid, N, K, A)

    if Answer == False:
        LEFT = Mid + 1
    if Answer == True:
        RIGHT = Mid

#出力
print(LEFT) #ギリギリTrueを出力