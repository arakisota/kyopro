"""
int(A, K)でK進法の数値を10進法の数値に変換することができる
"""

K = int(input())
A, B = map(str, input().split())
ans_A = 0
ans_B = 0
for i in range(len(A)):
    ans_A += pow(K, len(A)- i - 1) * int(A[i])
for j in range(len(B)):
    ans_B += pow(K, len(B)- j - 1) * int(B[j])

print(ans_A*ans_B)