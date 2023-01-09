ans = list(map(int, input().split()))
if len(set(ans)) == 3:
    print(0)
else:
    temp = 2 * sum(list(set(ans))) - sum(ans)
    if temp <= 0:
        print(ans[0])
    else:
        print(temp)