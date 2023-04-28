N = int(input())
S = input()

ind = S.index("*")
if S[:ind].count("|") == 1:
    print("in")
else:
    print("out")