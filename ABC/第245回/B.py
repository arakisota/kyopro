N = int(input())
A = list(map(int, input().split()))

num = [i for i in range(N+1)]
ans = sorted(list(set(num) - set(A)))[0]

print(ans)