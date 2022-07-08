# https://www.acmicpc.net/problem/1931
import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

meetings = sorted(meetings, key= lambda x: (x[1], x[0]))

cnt = 0
cur_end = 0
for start, end in meetings:
    if start >= cur_end:
        cur_end = end
        cnt += 1
print(cnt)