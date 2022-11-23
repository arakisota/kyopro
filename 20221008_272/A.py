N = int(input())
A = list(map(int, input().split()))

Answer = 0
for i in range(N):
    Answer += A[i]

print(Answer)