#入力
N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

"""
#これだとメモリが足りない
judge = [0] 
dp = [1] * (10**9)
for i in range(N):
    dp[A[i]-1] = max(B[i-1], dp[A[i]-1])

print(max(dp))
"""
numA_list = [1]
numB_list = [1]
for i in N:
    if B[i] in A:
        numA_list.append(B[i])
        numB_list.append(A[i])

print(max(numB_list))