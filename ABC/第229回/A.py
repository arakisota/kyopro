S1 = input()
S2 = input()
S1 += S2
no = ["....", "...#", "..#.", ".#..", "#...", ".##.", "#..#"]
if S1 in set(no):
    print("No")
else:
    print("Yes")