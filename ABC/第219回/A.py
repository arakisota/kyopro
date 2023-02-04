X = int(input())
if X >= 90:
    print("expert")
elif X < 40:
    print(40 - X)
elif 40 <= X < 70:
    print(70 - X)
else:
    print(90 - X)