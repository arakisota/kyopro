N = int(input())

moji = set()
score = 0
ind = 0
for i in range(N):
    S, T = input().split()
    if S not in moji:
        moji.add(S)
        if score < int(T):
            score = int(T)
            ind = i+1

print(ind)