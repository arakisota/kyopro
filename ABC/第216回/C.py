N = int(input())

temp = 1
i = 0
while N >= temp:
    temp *= 2
    if temp >= N:
        break
    i += 1
diff = N - pow(2, i)
ans = "A" + "B"*i + "A"*diff
print(ans)