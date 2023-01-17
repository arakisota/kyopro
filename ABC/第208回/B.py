"""
from math import factorial
→これで階乗の計算はできる
"""

P = int(input())
money = [1, 2, 6, 24, 120, 720, 5040, 5040*8, 5040*8*9, 5040*8*9*10]

def comp(P, money):
    for i in range(len(money)):
        if money[i] > P:
            return money[i-1]
    return money[-1]
count = 0
while P != 0:
    P -= comp(P, money)
    count += 1

print(count)