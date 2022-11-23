"""
二次元配列にして、一つずつ処理する
"""

N, M = map(int, input().split())

li = [[False]*(N+1) for i in range(N+1)]
for i in range(M):
    kx = list(map(int, input().split()))
    L = kx[0]
    x = kx[1:]
    for j in range(L):
        for k in range(L):
            li[x[j]][x[k]] = True
            
for i in range(1, N+1):
    if sum(li[i]) != N:
        print('No')
        exit()
        
print('Yes')