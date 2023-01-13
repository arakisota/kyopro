"""
（別解）
全体から最小のカードを引く
"""
A, B, C = map(int, input().split())
ab = A + B
ac = A + C
bc = B + C

ans = [ab, ac, bc]
print(max(ans))