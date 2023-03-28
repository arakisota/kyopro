from heapq import heapify, heappush, heappop

N, Q = map(int, input().split())
p = [i for i in range(1, N+1)]
p2 = []
ans = []
heapify(p)
heapify(p2)

for i in range(Q):
    #print(p)
    #print(p2)
    query = input().split()
    if query[0] == "1":
        tmp = heappop(p)
        heappush(p2, tmp)
    elif query[0] == "2":
        p2.remove(int(query[1]))
    else:
        print(min(p2))