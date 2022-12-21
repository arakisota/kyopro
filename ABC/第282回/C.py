n = int(input())
s = input()
ans = [""] * n

is_quoted = False

for i, c in enumerate(s):
    if c == '"':
      is_quoted = not is_quoted
      ans[i] = c
    elif c == ',':
      ans[i] = c if is_quoted else '.'
    else:
      ans[i] = c

print("".join(ans))