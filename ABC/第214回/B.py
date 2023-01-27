"""
・愚直に全探索する
→forループの範囲をrange(100)にすると0~99になってしまうため、range(101)にする必要がある
"""

S, T = map(int, input().split())
cnt = 0
for a in range(100+1):
    for b in range(100-a+1):
        for c in range(100-a-b+1):
            if a+b+c <= S and a*b*c <= T:
                cnt += 1

print(cnt)