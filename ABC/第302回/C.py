from itertools import permutations

def check_possible_strings(strings):
    for perm in permutations(strings):
        possible = True
        for i in range(len(perm) - 1):
            count_diff = sum(a != b for a, b in zip(perm[i], perm[i+1]))
            if count_diff != 1:
                possible = False
                break
        if possible:
            return True
    return False

N, M = map(int, input().split())

S = []
for _ in range(N):
    S.append(input())

if check_possible_strings(S):
    print("Yes")
else:
    print("No")