def remove_parentheses(S):
    stack = []
    result = []
    tmp = []
    for char in S:
        if char == ')' and stack and stack[-1] == '(':
            stack.pop()
            result.append(tmp)
            tmp = []
        elif char == "(":
            stack.append(char)
            flag = True
        if stack and char not in set(["(", ")"]):
            tmp.append(char)

    return 

# 入力の受け取り
N = int(input())
S = input()

stack = []
result = str()
flag = False
for char in S:
    if not flag and char not in set(["(", ")"]):
        result += char
    if flag and ")":
