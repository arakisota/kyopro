N = int(input())
A = list(map(int, input().split()))

A.sort()
tmp = []

count = 0
for i in range(1, N):
    count += 1
    if A[i] - A[i-1] != 0:
        tmp.append(count)
        count = 0
    
if tmp[-1] <= N - 3:
    tmp.append(count+1)

ans = 0
for num in tmp:
    if num >= 3:
        ans += (num * (num-1) * (num-2) / 6) 
print(int(ans))

"""
この問題は個数だけ数えればいい。かつ100までになっているから
count = [0] * 101として良い
for i in range(N):
    count[A[i]] += 1
for i in range(1, 101):
    Answer += count[i] * (count[i]-1) * (count[i]-2) // 6

でACできる
"""