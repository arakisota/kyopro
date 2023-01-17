N = int(input())
S = input()
for i in range(1, N):
    count = 0
    j = 0
    while i+j <= N-1:
        if S[j] == S[j+i]:
            break
        else:
            count += 1
        j += 1
    print(count)