import itertools
import bisect
N = int(input())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

time = [0] * N
for i in range(N):
    time[i] = A[i] / B[i]
sum_time = sum(time)
meet = sum_time / 2
acm_time = list(itertools.accumulate(time))
acm_dist = list(itertools.accumulate(A))
idx = bisect.bisect_left(acm_time, meet)
if idx == 0:
    meet_dist = meet * B[0]
else:
    meet_dist = (meet - acm_time[idx-1])*B[idx] + acm_dist[idx-1]
print(meet_dist)