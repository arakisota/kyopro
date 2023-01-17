N , X = map(int, input().split())
A = list(map(int, input().split()))

nebiki = len(A) // 2
price = sum(A) - nebiki

if price > X:
    print("No")
else:
    print("Yes")