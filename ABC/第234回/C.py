K = int(input())
bin_num = str(bin(K)[2:])
ans = str()

for s in bin_num:
    if s == "1":
        ans += "2"
    else:
        ans += "0"

print(ans)