"""
文字列の比較は辞書順で比較される
→また文字列の比較では、Unicode Pointで比較される
"""
S, T = map(str, input().split())
if S < T:
    print("Yes")
else:
    print("No")