V, *shampoo = map(int, input().split())
N = 10**6
ans = 2
for s in range(N):
    V -= shampoo[s%3]
    if V < 0:
        ans = s % 3
        break

if ans == 0:
    print("F")
elif ans == 1:
    print("M")
else:
    print("T")