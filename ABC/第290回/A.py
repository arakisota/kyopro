N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

score = 0
for b in B:
    score += A[b-1]

print(score)