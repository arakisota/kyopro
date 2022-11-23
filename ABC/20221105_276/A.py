S = input()

answer_list = []
count = 1
count_list = []
for i in S:
    if i == "a":
        answer_list.append(i)
        count_list.append(count)
    count += 1

if answer_list == []:
    print(-1)
else:
    print(count_list[-1])