N = int(input())

price = (1.08 * N) // 1
if price < 206:
    print("Yay!")
elif price == 206:
    print("so-so")
else:
    print(":(")