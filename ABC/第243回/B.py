N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt1 = 0
for i in range(N):
    if A[i] == B[i]:
        cnt1 += 1

cnt2 = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[j] and i != j:
            cnt2 += 1

print(cnt1)
print(cnt2)