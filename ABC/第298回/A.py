N = int(input())
S = input()

FLAG = True
good = 0
for s in S:
    if s == "x":
        FLAG = False
        break
    if s == "o":
        good += 1

if FLAG:
    if good > 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")