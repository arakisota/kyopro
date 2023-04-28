"""
制約が2*10^5だからそのままソートでいける
"""
import bisect
from collections import defaultdict

N = int(input())
Q = int(input())
box = defaultdict(list)
num = defaultdict(set)
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        box[query[2]].append(query[1])
        num[query[1]].add(query[2])
    elif query[0] == 2:
        for val in sorted(box[query[1]]):
            print(val, end=" ")
    else:
        for val in sorted(list(num[query[1]])):
            print(val, end=" ")