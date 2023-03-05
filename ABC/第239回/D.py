from collections import Counter
A, B, C, D = map(int, input().split())

def judge(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

ans = False
cnt = Counter()
for i in range(A, B+1):
    for j in range(C, D+1):
        if not judge(i+j):
            cnt[i] += 1
    if cnt[i] == D - C + 1:
        ans = True
        break

if ans == False:
    print("Aoki")
else:
    print("Takahashi")