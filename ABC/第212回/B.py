"""
以下のようにif分で条件分岐で答えても良いが、今回の場合だと弱いパスワードが20種類しかないため、全て先に列挙してしまうやり方もある
"""

X = list(input())

ans = 0
if len(set(X)) == 1:
    print("Weak")
else:
    for i in range(3):
        if int(X[i]) < 9:
            if int(X[i+1]) - int(X[i]) == 1:
                ans += 1
        else:
            if int(X[i+1])== 0:
                ans += 1
    if ans == 3:
        print("Weak")
    else:
        print("Strong")